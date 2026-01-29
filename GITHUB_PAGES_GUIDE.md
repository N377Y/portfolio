# 🚀 Guide de Déploiement GitHub Pages

## ✅ Fini avec GCP ! Bienvenue sur GitHub Pages

GitHub Pages est **100% gratuit**, **simple** et **rapide**. Pas de configuration compliquée !

## 📝 Ce qui a été fait

✅ Site statique généré (`index.html`)  
✅ Fichiers de configuration créés (`.nojekyll`, `_config.yml`)  
✅ Script de déploiement prêt (`deploy-github.sh`)  
✅ Chemin du CV corrigé (`CV_Marie-Ange_KUITCHE.pdf`)  

## 🚀 Déploiement en 3 Étapes

### Étape 1 : Créer un Repository sur GitHub

1. Allez sur [github.com/new](https://github.com/new)
2. Nommez votre repository : `Portfolio` (ou autre nom)
3. **Public** (obligatoire pour GitHub Pages gratuit)
4. **Ne cochez aucune option** (pas de README, .gitignore, etc.)
5. Cliquez sur **Create repository**

### Étape 2 : Déployer avec le Script

```bash
./deploy-github.sh
```

Le script vous demandera :
- **Nom du repository** : entrez `Portfolio` (ou le nom que vous avez choisi)
- **Nom d'utilisateur GitHub** : entrez votre username GitHub

Ensuite il fera tout automatiquement :
- ✅ Initialise Git
- ✅ Configure le remote
- ✅ Commit les fichiers
- ✅ Push vers GitHub

### Étape 3 : Activer GitHub Pages

1. Allez sur votre repository : `https://github.com/VOTRE-USERNAME/Portfolio`
2. Cliquez sur **Settings** (⚙️)
3. Dans le menu de gauche, cliquez sur **Pages**
4. Dans **Source**, sélectionnez :
   - Branch: `main`
   - Folder: `/ (root)`
5. Cliquez sur **Save**

**C'est tout ! 🎉**

Attendez 1-2 minutes et votre site sera en ligne à :
```
https://VOTRE-USERNAME.github.io/Portfolio/
```

## 🎯 Exemple Complet

Si votre username GitHub est `marie-angekuitche` et votre repo est `Portfolio` :

```bash
# 1. Déployer
./deploy-github.sh

# Quand demandé:
# Repository name: Portfolio
# GitHub username: marie-angekuitche

# 2. Activer GitHub Pages sur:
# https://github.com/marie-angekuitche/Portfolio/settings/pages

# 3. Votre site sera accessible à:
# https://marie-angekuitche.github.io/Portfolio/
```

## 🔄 Mettre à Jour le Site

Pour mettre à jour votre portfolio :

```bash
# 1. Modifier les données dans main.py
# 2. Régénérer le site
python3 generate_static.py

# 3. Commit et push
git add index.html
git commit -m "Update portfolio"
git push

# Le site se met à jour automatiquement en 1-2 minutes !
```

## ✨ Avantages de GitHub Pages vs GCP

| Aspect | GitHub Pages | GCP Cloud Run |
|--------|--------------|---------------|
| **Prix** | 💚 Gratuit à vie | 💰 Payant (après crédits) |
| **Configuration** | ✅ Simple (3 clics) | ❌ Complexe (permissions, APIs, etc.) |
| **Déploiement** | ⚡ 1-2 minutes | 🐌 5-10 minutes |
| **Maintenance** | 😎 Aucune | 😓 Surveillance régulière |
| **Performance** | 🚀 Excellent (CDN global) | ✅ Bon |
| **SSL/HTTPS** | ✅ Automatique | ✅ Automatique |
| **Domaine custom** | ✅ Gratuit | 💰 Possible mais plus complexe |

## 🐛 Problèmes Courants

### Le site affiche une 404
- Attendez 2-3 minutes après le premier déploiement
- Vérifiez que GitHub Pages est bien activé dans Settings > Pages
- Vérifiez que la branche `main` est sélectionnée

### Les styles ne chargent pas
- Vérifiez que le fichier `static/css/style.css` a bien été pushé
- Videz le cache : Cmd+Shift+R (Mac) ou Ctrl+Shift+R (Windows)

### Le CV ne charge pas
- Vérifiez que `static/cv/CV_Marie-Ange_KUITCHE.pdf` existe
- Attention à la casse : Linux (GitHub) est sensible à la casse

### "Permission denied" lors du push
```bash
# Solution 1: Utiliser un token GitHub
# Allez sur: https://github.com/settings/tokens
# Générez un token avec scope "repo"
# Utilisez-le comme mot de passe lors du push

# Solution 2: Utiliser SSH
git remote set-url origin git@github.com:VOTRE-USERNAME/Portfolio.git
```

## 📚 Ressources

- [Documentation GitHub Pages](https://docs.github.com/pages)
- [Configurer un domaine personnalisé](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Tokens GitHub](https://github.com/settings/tokens)

## 🎉 Prêt à Déployer !

```bash
./deploy-github.sh
```

Votre portfolio sera en ligne en moins de 5 minutes ! 🚀

---

**Besoin d'aide ?** Consultez la [documentation officielle](https://docs.github.com/pages) ou ouvrez une issue.

