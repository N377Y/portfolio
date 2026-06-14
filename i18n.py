"""
Smart i18n module for the portfolio.

Strategy (the same one used by most professional sites):
    1. We keep ONE source of truth in French in `main.py`.
    2. At application startup, every translatable French string is sent to
       Google Translate (via the free `deep-translator` library) to produce
       its English counterpart.
    3. Each translation is cached on disk (`translations_cache.json`) so the
       network is hit only ONCE per unique source string. Subsequent boots
       are instant and work fully offline.
    4. A `translations_overrides.json` file lets you override any
       auto-translation with a hand-polished version. Overrides always win.
    5. A small set of deterministic rules handle things the translator does
       poorly (e.g. French month names in date ranges).

The result: `enrich_with_translations(data)` returns the same data structure
with `_en` sibling keys injected next to every translatable field, ready to
be consumed by the Jinja templates that already use `data.bio_en | default(...)`.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
from copy import deepcopy
from typing import Any

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# Files
# --------------------------------------------------------------------------- #
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(_BASE_DIR, "translations_cache.json")
OVERRIDES_FILE = os.path.join(_BASE_DIR, "translations_overrides.json")

# --------------------------------------------------------------------------- #
# Deterministic French -> English month mapping (no API call needed)
# --------------------------------------------------------------------------- #
_MONTHS = {
    "janvier": "January", "février": "February", "fevrier": "February",
    "mars": "March", "avril": "April", "mai": "May", "juin": "June",
    "juillet": "July", "août": "August", "aout": "August",
    "septembre": "September", "octobre": "October",
    "novembre": "November", "décembre": "December", "decembre": "December",
}
_MONTH_REGEX = re.compile(
    r"\b(" + "|".join(_MONTHS.keys()) + r")\b",
    flags=re.IGNORECASE,
)
_PRESENT_REGEX = re.compile(r"\bPrésent\b|\bPresent\b", flags=re.IGNORECASE)


def _translate_period(text: str) -> str:
    """Translate a French date range to English without calling any API."""
    def _replace_month(match: re.Match) -> str:
        word = match.group(0)
        english = _MONTHS[word.lower()]
        # preserve title case (Septembre -> September)
        return english if word[0].isupper() else english.lower()

    text = _MONTH_REGEX.sub(_replace_month, text)
    text = _PRESENT_REGEX.sub("Present", text)
    return text


# --------------------------------------------------------------------------- #
# Cache + overrides
# --------------------------------------------------------------------------- #
def _load_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return {}


def _save_json(path: str, data: dict) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
    except OSError as exc:
        logger.warning("Could not write %s: %s", path, exc)


def _hash_key(text: str) -> str:
    """Stable cache key that survives JSON encoding."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


# --------------------------------------------------------------------------- #
# Lazy translator (so a missing dependency doesn't crash the app)
# --------------------------------------------------------------------------- #
_translator = None
_translator_failed = False


def _get_translator():
    global _translator, _translator_failed
    if _translator is not None or _translator_failed:
        return _translator
    try:
        from deep_translator import GoogleTranslator
        _translator = GoogleTranslator(source="fr", target="en")
    except Exception as exc:  # pragma: no cover - dependency / network issues
        logger.warning("deep-translator unavailable, FR will be used as fallback: %s", exc)
        _translator_failed = True
        _translator = None
    return _translator


# --------------------------------------------------------------------------- #
# Core translation primitive
# --------------------------------------------------------------------------- #
class _TranslationContext:
    """Holds the cache + overrides for one enrichment pass."""

    def __init__(self) -> None:
        self.cache: dict = _load_json(CACHE_FILE)
        self.overrides: dict = _load_json(OVERRIDES_FILE)
        self.dirty = False
        self.api_calls = 0

    def translate(self, text: str) -> str:
        if not isinstance(text, str) or not text.strip():
            return text

        # 1. Manual override always wins
        if text in self.overrides:
            return self.overrides[text]

        # 2. Cache lookup
        key = _hash_key(text)
        if key in self.cache:
            return self.cache[key]

        # 3. Network call
        translator = _get_translator()
        if translator is None:
            return text  # graceful fallback: keep French
        try:
            translated = translator.translate(text)
            if not translated:
                return text
            self.cache[key] = translated
            self.dirty = True
            self.api_calls += 1
            return translated
        except Exception as exc:  # pragma: no cover
            logger.warning("Translation failed for %r: %s", text[:60], exc)
            return text

    def flush(self) -> None:
        if self.dirty:
            _save_json(CACHE_FILE, self.cache)


# --------------------------------------------------------------------------- #
# Schema: which fields of `portfolio_data` need translating
#
# `text`   -> send through the translator
# `period` -> deterministic month translation (no API)
# Anything not listed is left untouched (names, URLs, tech labels, icons, ...)
# --------------------------------------------------------------------------- #
_TRANSLATABLE = {
    "title": "text",
    "bio": "text",

    "soft_skills.*.name": "text",
    "soft_skills.*.description": "text",

    "languages.*.name": "text",
    "languages.*.level": "text",

    "experiences.*.title": "text",
    "experiences.*.description": "text",
    "experiences.*.period": "period",
    "experiences.*.achievements.*": "text",

    "education.*.degree": "text",
    "education.*.description": "text",
    "education.*.period": "period",

    "certifications.*.description": "text",

    "hobbies.*.name": "text",
    "hobbies.*.description": "text",

    "references.*.title": "text",

    "projects.*.title": "text",
    "projects.*.description": "text",
    "projects.*.details.objectif": "text",
    "projects.*.details.features.*": "text",
    "projects.*.details.challenges.*": "text",
    "projects.*.details.results": "text",
}


def _path_matches(path: str, pattern: str) -> bool:
    p_parts = path.split(".")
    pat_parts = pattern.split(".")
    if len(p_parts) != len(pat_parts):
        return False
    return all(pp == "*" or pp == pp2 for pp, pp2 in zip(pat_parts, p_parts))


def _rule_for(path: str) -> str | None:
    for pattern, rule in _TRANSLATABLE.items():
        if _path_matches(path, pattern):
            return rule
    return None


# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #
def enrich_with_translations(data: dict) -> dict:
    """Return a deep copy of `data` with `<field>_en` keys added everywhere
    a French translatable string was found."""

    out = deepcopy(data)
    ctx = _TranslationContext()

    def _translate_value(value: str, rule: str) -> str:
        if rule == "period":
            return _translate_period(value)
        return ctx.translate(value)

    def _walk(node: Any, path: str) -> None:
        if isinstance(node, dict):
            # Snapshot keys first because we are going to mutate the dict
            for key in list(node.keys()):
                child_path = f"{path}.{key}" if path else key
                child = node[key]

                # Already-provided English override (e.g. existing `name_en`) wins
                en_key = f"{key}_en"
                if isinstance(child, str):
                    rule = _rule_for(child_path)
                    if rule and en_key not in node:
                        node[en_key] = _translate_value(child, rule)
                elif isinstance(child, list):
                    rule = _rule_for(child_path + ".*")
                    if rule and all(isinstance(x, str) for x in child) and en_key not in node:
                        node[en_key] = [_translate_value(x, rule) for x in child]
                    else:
                        for idx, item in enumerate(child):
                            _walk(item, f"{child_path}.{idx}")
                elif isinstance(child, dict):
                    _walk(child, child_path)

    _walk(out, "")

    ctx.flush()
    if ctx.api_calls:
        logger.info("i18n: %s new translation(s) cached", ctx.api_calls)
    return out


__all__ = ["enrich_with_translations"]

