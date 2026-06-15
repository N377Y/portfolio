// ============================================
// MODERN PORTFOLIO - ADVANCED JAVASCRIPT
// ============================================

// ============================================
// I18N (FR / EN LANGUAGE SWITCHER)
// ============================================
// Smart hybrid system:
//   - Server-side: i18n.py auto-translates `portfolio_data` and injects
//     `<field>_en` siblings (cached on disk, manual overrides supported).
//   - Client-side: every translatable element has `data-fr` / `data-en`
//     (or `data-fr-html` / `data-en-html` for content with markup).
//     This module swaps content live without reloading the page.
const I18N = (() => {
    const STORAGE_KEY = 'portfolio.lang';
    const SUPPORTED = ['fr', 'en'];
    const subscribers = [];
    let currentLang = null; // last language actually applied

    function getLang() {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved && SUPPORTED.includes(saved)) return saved;
        // Auto-detect from browser, default to FR
        const nav = (navigator.language || 'fr').slice(0, 2).toLowerCase();
        return SUPPORTED.includes(nav) ? nav : 'fr';
    }

    function applyLanguage(lang) {
        if (!SUPPORTED.includes(lang)) lang = 'fr';
        const changed = lang !== currentLang;

        // 1. Plain text swaps. We skip `.typing-text` because the typing
        //    animation reads the source from data-fr/data-en itself and
        //    manages textContent on its own (otherwise the user briefly
        //    sees the full new-language text before the animation clears it).
        document.querySelectorAll('[data-fr][data-en]').forEach(el => {
            if (el.classList.contains('typing-text')) return;
            const value = el.dataset[lang];
            if (value !== undefined) el.textContent = value;
        });

        // 2. HTML swaps (content with inline markup like <i>, <strong>, ...)
        document.querySelectorAll('[data-fr-html][data-en-html]').forEach(el => {
            const value = lang === 'fr' ? el.dataset.frHtml : el.dataset.enHtml;
            if (value !== undefined) el.innerHTML = value;
        });

        // 3. <html lang="..."> for accessibility / SEO
        document.documentElement.lang = lang;

        // 4. Toggle the active button
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        // 5. Persist
        localStorage.setItem(STORAGE_KEY, lang);
        currentLang = lang;

        // 6. Notify subscribers ONLY when the language actually changes.
        //    This avoids re-triggering the typing animation on every
        //    redundant applyLanguage() call during page bootstrap, which
        //    otherwise cancelled mid-flight and left text like "Déve".
        if (changed) {
            subscribers.forEach(fn => {
                try { fn(lang); } catch (e) { console.error('[i18n] subscriber failed:', e); }
            });
        }
    }

    function onChange(fn) {
        if (typeof fn === 'function') subscribers.push(fn);
    }

    function init() {
        applyLanguage(getLang());
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', () => applyLanguage(btn.dataset.lang));
        });
    }

    return { getLang, applyLanguage, onChange, init };
})();

// Apply language ASAP (before assets fully load) so users never see a flash
// of the wrong language. Then re-bind click handlers on DOMContentLoaded.
I18N.applyLanguage(I18N.getLang());
document.addEventListener('DOMContentLoaded', I18N.init);

// ============================================
// PAGE LOADING
// ============================================
window.addEventListener('load', () => {
    setTimeout(() => {
        document.body.classList.remove('loading');
    }, 1500);
});

// ============================================
// CUSTOM CURSOR
// ============================================
const cursor = document.querySelector('.cursor-dot');
const cursorOutline = document.querySelector('.cursor-outline');
const customCursor = document.querySelector('.custom-cursor');

let mouseX = 0, mouseY = 0;
let outlineX = 0, outlineY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    cursor.style.left = mouseX + 'px';
    cursor.style.top = mouseY + 'px';
});

function animateCursorOutline() {
    outlineX += (mouseX - outlineX) * 0.1;
    outlineY += (mouseY - outlineY) * 0.1;

    cursorOutline.style.left = outlineX + 'px';
    cursorOutline.style.top = outlineY + 'px';

    requestAnimationFrame(animateCursorOutline);
}

animateCursorOutline();

// Cursor hover effects
const hoverElements = document.querySelectorAll('a, button, .project-card, .skill-item');
hoverElements.forEach(el => {
    el.addEventListener('mouseenter', () => customCursor.classList.add('hover'));
    el.addEventListener('mouseleave', () => customCursor.classList.remove('hover'));
});

// ============================================
// THEME TOGGLE
// ============================================
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const icon = themeToggle.querySelector('i');

const savedTheme = localStorage.getItem('theme') || 'light';
if (savedTheme === 'dark') {
    body.classList.add('dark-mode');
    icon.classList.replace('fa-moon', 'fa-sun');
}

themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');

    if (body.classList.contains('dark-mode')) {
        icon.classList.replace('fa-moon', 'fa-sun');
        localStorage.setItem('theme', 'dark');
    } else {
        icon.classList.replace('fa-sun', 'fa-moon');
        localStorage.setItem('theme', 'light');
    }
});


// ============================================
// NAVIGATION
// ============================================
const nav = document.querySelector('.nav');
const navItems = document.querySelectorAll('.nav-item');
const sections = document.querySelectorAll('section[id]');

// Scroll effect
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }

    // Active nav item
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === `#${current}`) {
            item.classList.add('active');
        }
    });
});

// Smooth scrolling
navItems.forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = item.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        targetSection.scrollIntoView({ behavior: 'smooth' });
    });
});

// Mobile menu toggle
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.querySelector('.nav-menu');

menuToggle?.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    menuToggle.classList.toggle('active');
});

// ============================================
// WEBGL BACKGROUND (Three.js)
// ============================================
const canvas = document.getElementById('webgl-canvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
camera.position.z = 5;

// Create particle system
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 1000;
const posArray = new Float32Array(particlesCount * 3);

for (let i = 0; i < particlesCount * 3; i++) {
    posArray[i] = (Math.random() - 0.5) * 10;
}

particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

const particlesMaterial = new THREE.PointsMaterial({
    size: 0.005,
    color: 0x6366f1,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
});

const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);

// Mouse interaction
let mouseXThree = 0;
let mouseYThree = 0;

document.addEventListener('mousemove', (e) => {
    mouseXThree = (e.clientX / window.innerWidth) * 2 - 1;
    mouseYThree = -(e.clientY / window.innerHeight) * 2 + 1;
});

// Animation loop
function animate() {
    requestAnimationFrame(animate);

    particlesMesh.rotation.y += 0.0005;
    particlesMesh.rotation.x = mouseYThree * 0.1;
    particlesMesh.rotation.y += mouseXThree * 0.05;

    renderer.render(scene, camera);
}

animate();

// Resize handler
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// ============================================
// TYPING EFFECT (language-aware)
// ============================================
const typingText = document.querySelector('.typing-text');
let typingToken = 0; // increment to cancel any in-flight animation

function startTypingAnimation() {
    if (!typingText) return;
    const lang = I18N.getLang();
    // Read the source text from the data-* attributes (NOT textContent, which
    // gets cleared while typing). Fall back to the original text content.
    const source = typingText.dataset[lang] || typingText.textContent || '';

    typingToken += 1;
    const myToken = typingToken;
    typingText.textContent = '';
    let i = 0;

    function typeWriter() {
        if (myToken !== typingToken) return; // a newer animation has started
        if (i < source.length) {
            typingText.textContent += source.charAt(i);
            i += 1;
            setTimeout(typeWriter, 60);
        }
    }

    setTimeout(typeWriter, 300);
}

if (typingText) {
    setTimeout(startTypingAnimation, 500);
    I18N.onChange(startTypingAnimation);
}

// ============================================
// AOS (Animate On Scroll)
// ============================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('aos-animate');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('[data-aos]').forEach(el => {
    observer.observe(el);
});

// ============================================
// COUNTER ANIMATION
// ============================================
// Read the target number directly from the element's text (e.g. "3+", "15+").
// The HTML stays the single source of truth – no `data-target` to keep in sync,
// which is what caused the "NaN+" bug previously.
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;

        const counter = entry.target;
        const original = (counter.textContent || '').trim();
        const match = original.match(/\d+/);
        if (!match) {
            counterObserver.unobserve(counter);
            return;
        }
        const target = parseInt(match[0], 10);
        const suffix = original.slice(match.index + match[0].length); // keep "+" / "%" / ...
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.ceil(current) + suffix;
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target + suffix;
            }
        };

        updateCounter();
        counterObserver.unobserve(counter);
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-number').forEach(counter => {
    counterObserver.observe(counter);
});

// ============================================
// SKILL BARS ANIMATION
// ============================================
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const skillFill = entry.target;
            const level = skillFill.getAttribute('data-level');
            setTimeout(() => {
                skillFill.style.width = level + '%';
            }, 300);
            skillObserver.unobserve(skillFill);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.skill-fill').forEach(bar => {
    skillObserver.observe(bar);
});

// ============================================
// PARALLAX EFFECT
// ============================================
// NOTE: do NOT apply parallax to `.project-image`. The parent `.project-card`
// has `overflow: hidden`, so translating the inner image hides it as the user
// scrolls. We only animate the hero content here.
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const heroContent = document.querySelector('.hero-content');

    // Only apply parallax while the hero is still in (or near) the viewport,
    // otherwise the hero content would translate indefinitely.
    if (heroContent && scrolled < window.innerHeight) {
        heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
    } else if (heroContent) {
        heroContent.style.transform = '';
    }
});

// ============================================
// PROJECT CARDS 3D EFFECT
// ============================================
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * 5;
        const rotateY = ((x - centerX) / centerX) * -5;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
});

// ============================================
// SMOOTH REVEAL ANIMATIONS
// ============================================
const revealElements = document.querySelectorAll('.skill-item, .project-card, .contact-method, .stat-item');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, index * 100);
        }
    });
}, { threshold: 0.1 });

revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
    revealObserver.observe(el);
});

// ============================================
// PAGE TRANSITIONS
// ============================================
// Only handle in-page hash links (e.g. "#work").
// External links ("https://...") must not be treated as CSS selectors.
document.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Ignore empty / external links
        if (!href || href === '#' || !href.startsWith('#')) {
            return;
        }

        const target = document.getElementById(href.slice(1));
        if (!target) {
            return;
        }

        e.preventDefault();
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// ============================================
// PERFORMANCE OPTIMIZATIONS
// ============================================
// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Lazy load images when implemented
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ============================================
// CONSOLE MESSAGE
// ============================================
console.log(
    '%c👋 Hey there!',
    'font-size: 20px; font-weight: bold; color: #6366f1;'
);
console.log(
    '%cThanks for checking out my portfolio!',
    'font-size: 14px; color: #8b5cf6;'
);
console.log(
    '%c💼 Interested in working together? Get in touch!',
    'font-size: 12px; color: #ec4899;'
);

// ============================================
// EASTER EGG - Konami Code
// ============================================
let konamiCode = [];
const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);

    if (konamiCode.join('') === konamiSequence.join('')) {
        // Rainbow effect
        document.body.style.animation = 'rainbow 2s linear infinite';

        const style = document.createElement('style');
        style.textContent = `
            @keyframes rainbow {
                0% { filter: hue-rotate(0deg); }
                100% { filter: hue-rotate(360deg); }
            }
        `;
        document.head.appendChild(style);

        setTimeout(() => {
            document.body.style.animation = '';
            style.remove();
        }, 5000);

        console.log('🎉 Konami Code activated! 🌈');
    }
});

// ============================================
// PERFORMANCE MONITORING
// ============================================
if ('PerformanceObserver' in window) {
    const perfObserver = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
            if (entry.entryType === 'navigation') {
                console.log(`⚡ Page load time: ${entry.loadEventEnd - entry.fetchStart}ms`);
            }
        }
    });

    perfObserver.observe({ entryTypes: ['navigation'] });
}

// ============================================
// ACCESSIBILITY IMPROVEMENTS
// ============================================
// Focus visible for keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-nav');
    }
});

document.addEventListener('mousedown', () => {
    document.body.classList.remove('keyboard-nav');
});

// Add focus styles
const focusStyle = document.createElement('style');
focusStyle.textContent = `
    body.keyboard-nav *:focus {
        outline: 2px solid var(--accent-1);
        outline-offset: 2px;
    }
    
    body:not(.keyboard-nav) *:focus {
        outline: none;
    }
`;
document.head.appendChild(focusStyle);

// ============================================
// CERTIFICATION PREVIEW CLICK
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const certificationPreviews = document.querySelectorAll('.certification-preview');

    certificationPreviews.forEach(preview => {
        preview.addEventListener('click', function() {
            const iframe = this.querySelector('.certification-iframe');
            if (iframe) {
                const pdfUrl = iframe.src.split('#')[0]; // Remove parameters
                window.open(pdfUrl, '_blank');
            }
        });
    });

    // Gestion de la modal des projets
    const projectCards = document.querySelectorAll('.project-card');
    const modal = document.getElementById('projectModal');
    const closeBtn = document.querySelector('.project-modal-close');

    // Récupérer les données des projets depuis l'attribut data du HTML
    const projectsData = window.portfolioProjects || [];

    projectCards.forEach((card) => {
        card.addEventListener('click', function(e) {
            // Ne pas ouvrir la modal si on clique sur un lien
            if (e.target.closest('.project-link')) {
                return;
            }

            const projectIndexAttr = this.getAttribute('data-project-index');
            const projectIndex = Number(projectIndexAttr);

            if (!Number.isFinite(projectIndex) || projectIndex < 0 || projectIndex >= projectsData.length) {
                console.warn('[portfolio] Invalid project index:', projectIndexAttr, 'projectsData length:', projectsData.length);
                return;
            }

            const project = projectsData[projectIndex];
            if (!project) {
                console.warn('[portfolio] Missing project data at index:', projectIndex);
                return;
            }

            // Pick a string in the current language, falling back to FR
            const lang = I18N.getLang();
            const t = (frKey) => {
                if (lang === 'en') {
                    const en = project[frKey + '_en'];
                    if (en) return en;
                }
                return project[frKey] || '';
            };
            const tDetail = (frKey) => {
                const details = project.details || {};
                if (lang === 'en') {
                    const en = details[frKey + '_en'];
                    if (en) return en;
                }
                return details[frKey];
            };

            // Remplir la modal avec les données du projet
            const titleEl = document.getElementById('modalProjectTitle');
            const descEl = document.getElementById('modalProjectDescription');
            if (!titleEl || !descEl || !modal) {
                console.warn('[portfolio] Modal elements not found in DOM.');
                return;
            }

            titleEl.textContent = t('title');
            descEl.textContent = t('description');

            // Image
            const modalImage = document.getElementById('modalProjectImage');
            const modalImageContainer = modalImage ? modalImage.closest('.project-modal-image') : null;
            if (modalImage) {
                if (project.image) {
                    modalImage.src = project.image;
                    modalImage.alt = t('title');
                    modalImage.style.display = 'block';
                    if (modalImageContainer) {
                        modalImageContainer.style.display = 'block';
                        // Use the project's accent color for the banner background fallback
                        if (project.color) {
                            modalImageContainer.style.background = `linear-gradient(135deg, ${project.color}, #8b5cf6)`;
                        }
                    }
                } else {
                    modalImage.style.display = 'none';
                    if (modalImageContainer) {
                        modalImageContainer.style.display = 'none';
                    }
                }
            }

            // Détails supplémentaires
            if (project.details) {
                // Objectif
                const objectif = tDetail('objectif');
                if (objectif) {
                    const el = document.getElementById('modalProjectObjectif');
                    const section = document.getElementById('modalObjectifSection');
                    if (el && section) {
                        el.textContent = objectif;
                        section.style.display = 'block';
                    }
                } else {
                    const section = document.getElementById('modalObjectifSection');
                    if (section) section.style.display = 'none';
                }

                // Fonctionnalités clés
                const features = tDetail('features');
                if (features && features.length > 0) {
                    const featuresList = document.getElementById('modalProjectFeatures');
                    const section = document.getElementById('modalFeaturesSection');
                    if (featuresList && section) {
                        featuresList.innerHTML = '';
                        features.forEach(feature => {
                            const li = document.createElement('li');
                            li.textContent = feature;
                            featuresList.appendChild(li);
                        });
                        section.style.display = 'block';
                    }
                } else {
                    const section = document.getElementById('modalFeaturesSection');
                    if (section) section.style.display = 'none';
                }

                // Défis techniques
                const challenges = tDetail('challenges');
                if (challenges && challenges.length > 0) {
                    const challengesList = document.getElementById('modalProjectChallenges');
                    const section = document.getElementById('modalChallengesSection');
                    if (challengesList && section) {
                        challengesList.innerHTML = '';
                        challenges.forEach(challenge => {
                            const li = document.createElement('li');
                            li.textContent = challenge;
                            challengesList.appendChild(li);
                        });
                        section.style.display = 'block';
                    }
                } else {
                    const section = document.getElementById('modalChallengesSection');
                    if (section) section.style.display = 'none';
                }

                // Résultats
                const results = tDetail('results');
                if (results) {
                    const el = document.getElementById('modalProjectResults');
                    const section = document.getElementById('modalResultsSection');
                    if (el && section) {
                        el.textContent = results;
                        section.style.display = 'block';
                    }
                } else {
                    const section = document.getElementById('modalResultsSection');
                    if (section) section.style.display = 'none';
                }
            } else {
                // Cacher toutes les sections de détails si pas de détails
                const s1 = document.getElementById('modalObjectifSection');
                const s2 = document.getElementById('modalFeaturesSection');
                const s3 = document.getElementById('modalChallengesSection');
                const s4 = document.getElementById('modalResultsSection');
                if (s1) s1.style.display = 'none';
                if (s2) s2.style.display = 'none';
                if (s3) s3.style.display = 'none';
                if (s4) s4.style.display = 'none';
            }

            // Technologies
            const techContainer = document.getElementById('modalProjectTech');
            if (techContainer) {
                techContainer.innerHTML = '';
                (project.tech || []).forEach(tech => {
                    const badge = document.createElement('span');
                    badge.className = 'tech-badge';
                    badge.textContent = tech;
                    techContainer.appendChild(badge);
                });
            }

            // Liens
            const githubLink = document.getElementById('modalProjectGithub');
            const demoLink = document.getElementById('modalProjectDemo');

            if (githubLink) {
                if (project.github && project.github !== '#') {
                    githubLink.href = project.github;
                    githubLink.style.display = 'inline-flex';
                } else {
                    githubLink.style.display = 'none';
                }
            }

            if (demoLink) {
                if (project.demo && project.demo !== '#') {
                    demoLink.href = project.demo;
                    demoLink.style.display = 'inline-flex';
                } else {
                    demoLink.style.display = 'none';
                }
            }

            // Afficher la modal
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        });
    });

    // Fermer la modal
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    }

    // Fermer en cliquant à l'extérieur
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Fermer avec Échap
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Close the modal automatically when the user switches language so they
    // don't see a half-translated mix of FR/EN content.
    I18N.onChange(function () {
        if (modal && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
});

// ============================================
// SKILLS TOGGLE (Show More/Less) - language-aware
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('skillsToggleBtn');
    const toggleText = document.getElementById('skillsToggleText');
    const toggleIcon = document.getElementById('skillsToggleIcon');
    const extraCategories = document.querySelectorAll('.skills-extra-category');
    const skillsSection = document.getElementById('skills');

    if (!toggleBtn || extraCategories.length === 0) return;

    let isExpanded = false;

    function updateToggleLabel() {
        if (!toggleBtn || !toggleText) return;
        const lang = I18N.getLang();
        const key = (lang === 'en' ? 'en' : 'fr') + (isExpanded ? 'Expanded' : 'Collapsed');
        const label = toggleBtn.dataset[key];
        if (label) toggleText.textContent = label;
    }

    toggleBtn.addEventListener('click', function() {
        isExpanded = !isExpanded;

        // Toggle classe sur la section pour révéler Frameworks/Tools sur mobile
        if (skillsSection) {
            skillsSection.classList.toggle('skills-expanded', isExpanded);
        }

        extraCategories.forEach(category => {
            if (isExpanded) {
                category.style.display = 'block';
                setTimeout(() => {
                    category.style.opacity = '1';
                    category.style.transform = 'translateY(0)';
                }, 10);
            } else {
                category.style.opacity = '0';
                category.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    category.style.display = 'none';
                }, 300);
            }
        });

        updateToggleLabel();
        if (toggleIcon) {
            if (isExpanded) {
                toggleIcon.classList.replace('fa-chevron-down', 'fa-chevron-up');
            } else {
                toggleIcon.classList.replace('fa-chevron-up', 'fa-chevron-down');
            }
        }
    });

    // Refresh label when the user switches language
    I18N.onChange(updateToggleLabel);
    updateToggleLabel();
});

