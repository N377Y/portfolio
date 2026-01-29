# 🌟 Portfolio - Marie-Ange KUITCHE

Portfolio professionnel moderne et interactif présentant mes compétences, expériences et projets.

## 🚀 Voir le Portfolio en Ligne

🌐 **[Visitez mon portfolio](https://n377y.github.io/portfolio/)**

> *Une fois déployé sur GitHub Pages*

## 📋 À Propos

Développeuse Full Stack spécialisée en QA & Test Automation avec une passion pour l'IA et les architectures cloud-natives. Ce portfolio présente:

- 💼 Mon expérience professionnelle
- 🛠️ Mes compétences techniques (Python, JavaScript, React, Flask, etc.)
- 🎓 Ma formation et certifications (ISTQB, Google Cloud Digital Leader)
- 📂 Mes projets récents
- 📄 Mon CV téléchargeable

## 🎨 Fonctionnalités

- ✨ Design moderne et épuré avec animations fluides
- 📱 100% responsive (mobile, tablette, desktop)
- 🌓 Mode sombre/clair
- 🎯 Navigation intuitive
- 🚀 Performance optimisée
- 🎨 Effets visuels WebGL (Three.js)
- 📊 Visualisation interactive des compétences
- 📥 CV téléchargeable en PDF

## 🛠️ Technologies Utilisées

### Frontend
- HTML5, CSS3, JavaScript (ES6+)
- Three.js pour les effets WebGL
- Font Awesome pour les icônes
- AOS (Animate On Scroll) pour les animations
- Google Fonts (Inter, Space Grotesk)

### Backend (Version Flask - optionnelle)
- Python 3.11+
- Flask
- Jinja2

### Déploiement
- GitHub Pages (version statique)
- Hébergement gratuit et rapide

## 📂 Structure du Projet

```
Portfolio/
├── index.html              # Page principale (générée)
├── static/
│   ├── css/
│   │   └── style.css      # Styles personnalisés
│   ├── js/
│   │   └── script.js      # JavaScript personnalisé
│   ├── images/
│   │   ├── profile.png    # Photo de profil
│   │   └── ...
│   ├── cv/
│   │   └── CV_Marie-Ange_KUITCHE.pdf
│   ├── projets/           # Images des projets
│   │   ├── footelly.png
│   │   ├── HackAtassa.png
│   │   └── Optimious.png
│   └── certifications/    # Certificats PDF
│       ├── ISTQB.pdf
│       ├── CloudDigitalLeader.pdf
│       └── Numerique-responsable.pdf
├── templates/
│   └── index.html         # Template Jinja2
├── main.py                # Application Flask (dev)
├── generate_static.py     # Script de génération
├── deploy-github.sh       # Script de déploiement
├── .nojekyll             # Pour GitHub Pages
├── _config.yml           # Configuration GitHub Pages
└── README.md             # Ce fichier

```

## 🚀 Déploiement sur GitHub Pages

### Prérequis
- Python 3.11+
- Git
- Compte GitHub

### Étapes de Déploiement

1. **Cloner le repository (ou créer le vôtre)**
   ```bash
   git clone https://github.com/VOTRE-USERNAME/Portfolio.git
   cd Portfolio
   ```

2. **Générer et déployer**
   ```bash
   ./deploy-github.sh
   ```

3. **Configurer GitHub Pages**
   - Allez sur `https://github.com/VOTRE-USERNAME/Portfolio/settings/pages`
   - Dans "Source", sélectionnez la branche `main`
   - Laissez `/ (root)` comme dossier
   - Cliquez sur "Save"

4. **Attendez quelques minutes**
   - GitHub Pages prend 1-5 minutes pour déployer
   - Votre site sera disponible à `https://VOTRE-USERNAME.github.io/Portfolio/`

## 🔄 Mise à Jour du Portfolio

### Modifier le Contenu

1. **Modifier les données** dans `main.py` :
   ```python
   portfolio_data = {
       'name': 'Votre Nom',
       'title': 'Votre Titre',
       'bio': 'Votre bio...',
       # ... autres données
   }
   ```

2. **Régénérer le site statique** :
   ```bash
   python3 generate_static.py
   ```

3. **Redéployer** :
   ```bash
   git add .
   git commit -m "Update portfolio content"
   git push
   ```

### Modifier le Design

1. Éditez `static/css/style.css` pour les styles
2. Éditez `static/js/script.js` pour les fonctionnalités
3. Éditez `templates/index.html` pour la structure
4. Régénérez avec `python3 generate_static.py`

## 💡 Personnalisation

### Changer les Couleurs

Dans `static/css/style.css`, modifiez les variables CSS :

```css
:root {
    --primary-color: #6366f1;      /* Couleur principale */
    --secondary-color: #8b5cf6;    /* Couleur secondaire */
    --accent-color: #ec4899;       /* Couleur d'accent */
    /* ... */
}
```

### Ajouter des Projets

Dans `main.py`, ajoutez vos projets :

```python
'projects': [
    {
        'title': 'Nom du Projet',
        'description': 'Description...',
        'image': '/static/projets/mon-projet.png',
        'technologies': ['React', 'Python', 'Flask'],
        'github': 'https://github.com/...',
        'demo': 'https://...',
    },
]
```

### Mettre à Jour le CV

1. Remplacez le fichier `static/cv/CV_Marie-Ange_KUITCHE.pdf`
2. Ou renommez votre CV et mettez à jour le chemin dans `templates/index.html`

## 📱 Développement Local

### Avec Flask (mode développement)

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
python main.py

# Ouvrir dans le navigateur
open http://localhost:8080
```

### Version Statique (pour tester avant déploiement)

```bash
# Générer le site
python3 generate_static.py

# Ouvrir index.html dans un navigateur
open index.html
```

## 🐛 Dépannage

### Le site ne s'affiche pas correctement
- Vérifiez que tous les fichiers sont bien dans le dossier `static/`
- Vérifiez les chemins dans `index.html` (doivent être relatifs)
- Videz le cache du navigateur (Cmd+Shift+R)

### Les images ne chargent pas
- Vérifiez que les fichiers existent dans `static/images/`, `static/projets/`, etc.
- Vérifiez que les noms de fichiers correspondent (attention à la casse)

### Le CV ne s'affiche pas
- Vérifiez que `CV_Marie-Ange_KUITCHE.pdf` existe dans `static/cv/`
- Note: GitHub Pages est sensible à la casse (contrairement à macOS)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📧 Contact

- **Email**: marie-ange.kuitche@groupe-esigelec.org
- **LinkedIn**: [Marie-Ange KUITCHE](https://www.linkedin.com/in/marie-ange-nelly-kuitche-megouo-a49974226/)
- **GitHub**: [@marie-angekuitche](https://github.com/N377Y)

---

⭐ Si vous aimez ce portfolio, n'hésitez pas à lui donner une étoile !

**Fait avec ❤️ par Marie-Ange KUITCHE**

