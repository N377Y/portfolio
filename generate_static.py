"""
Script pour générer une version statique du portfolio pour GitHub Pages
"""

from jinja2 import Template
import json
import shutil
import os
import re

# Import des données du portfolio depuis main.py
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import portfolio_data

def generate_static_site():
    """Génère le site statique pour GitHub Pages"""

    print("🚀 Génération du site statique pour GitHub Pages...")

    # Lire le template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Créer le template Jinja2
    template = Template(template_content)

    # Rendre le template avec les données
    html_output = template.render(data=portfolio_data)

    # Nettoyer les attributs data-* i18n restants dans le HTML rendu
    html_output = re.sub(r'\sdata-(fr|en|i18n)="[^"]*"', '', html_output)

    # Créer le fichier index.html à la racine
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)

    print("✅ index.html généré avec succès!")

    # Créer un fichier _config.yml pour GitHub Pages (optionnel)
    config_content = """# GitHub Pages Configuration
theme: null
"""

    with open('_config.yml', 'w', encoding='utf-8') as f:
        f.write(config_content)

    print("✅ _config.yml créé!")

    # Créer un .nojekyll pour éviter le traitement Jekyll
    with open('.nojekyll', 'w') as f:
        f.write('')

    print("✅ .nojekyll créé!")

    print("\n🎉 Site statique généré avec succès!")
    print("\n📁 Fichiers créés:")
    print("   - index.html (à la racine)")
    print("   - _config.yml")
    print("   - .nojekyll")
    print("\n📂 Les fichiers static/ sont déjà présents")
    print("\n🚀 Prochaines étapes:")
    print("   1. Initialisez un repo Git (si pas déjà fait)")
    print("   2. Exécutez ./deploy-github.sh pour déployer")

if __name__ == '__main__':
    generate_static_site()
