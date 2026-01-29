#!/bin/bash

# Portfolio - Useful Commands
# Quick reference for common operations

cat << 'EOF'
╔════════════════════════════════════════════════════════════╗
║           PORTFOLIO - COMMANDES UTILES                     ║
╚════════════════════════════════════════════════════════════╝

🚀 DÉVELOPPEMENT LOCAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Démarrer le serveur :
    python main.py

  Démarrer sur un port différent :
    PORT=8000 python main.py

  Mode debug :
    FLASK_ENV=development python main.py


🐙 GITHUB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Setup automatique :
    ./init-github.sh

  Setup manuel :
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/USER/REPO.git
    git push -u origin main

  Mettre à jour :
    git add .
    git commit -m "Update portfolio"
    git push


☁️  GOOGLE CLOUD PLATFORM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Déploiement automatique :
    ./deploy.sh

  Cloud Run (manuel) :
    gcloud run deploy portfolio \
      --source . \
      --region europe-west1 \
      --allow-unauthenticated

  App Engine (manuel) :
    gcloud app deploy

  Voir les logs (Cloud Run) :
    gcloud run services logs read portfolio --region=europe-west1

  Voir les logs (App Engine) :
    gcloud app logs tail


🐳 DOCKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Build l'image :
    docker build -t portfolio .

  Lancer le container :
    docker run -p 8080:8080 portfolio

  Lancer avec variables d'environnement :
    docker run -p 8080:8080 -e FLASK_ENV=production portfolio


🧪 TESTS & VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Vérifier les imports :
    python -c "from main import app; print('✅ OK')"

  Tester l'API :
    curl http://127.0.0.1:5003/api/data

  Vérifier le HTML :
    curl http://127.0.0.1:5003 | head -50

  Vérifier les dépendances :
    pip check


📦 DÉPENDANCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Installer :
    pip install -r requirements.txt

  Mettre à jour :
    pip install --upgrade -r requirements.txt

  Exporter :
    pip freeze > requirements.txt

  Créer un environnement virtuel :
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows


🔧 CONFIGURATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Générer une clé secrète :
    python -c "import secrets; print(secrets.token_hex(32))"

  Changer le port :
    Modifier PORT dans config.py ou main.py

  Variables d'environnement (Linux/macOS) :
    export FLASK_ENV=production
    export SECRET_KEY=your-secret-key

  Variables d'environnement (Windows) :
    set FLASK_ENV=production
    set SECRET_KEY=your-secret-key


📊 MONITORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Voir les processus :
    ps aux | grep python

  Voir les ports utilisés :
    lsof -i :5003

  Tuer un processus sur le port 5003 :
    lsof -ti:5003 | xargs kill -9

  Statistiques serveur :
    curl http://127.0.0.1:5003 -w "@curl-format.txt" -o /dev/null -s


🧹 NETTOYAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Supprimer __pycache__ :
    find . -type d -name __pycache__ -exec rm -rf {} +

  Supprimer .pyc :
    find . -type f -name "*.pyc" -delete

  Nettoyage complet :
    rm -rf __pycache__ .pytest_cache .coverage htmlcov

  Supprimer .DS_Store (macOS) :
    find . -name .DS_Store -delete


📚 DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  README.md          - Documentation principale
  DEPLOYMENT.md      - Guide de déploiement
  QUICKSTART.md      - Guide de démarrage rapide
  CHANGELOG.md       - Historique des versions


🆘 AIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Flask :
    flask --help

  gcloud :
    gcloud --help
    gcloud run --help
    gcloud app --help

  Docker :
    docker --help
    docker run --help

  Git :
    git --help
    git commit --help


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Astuce : Ajoutez ce fichier à vos favoris pour un accès rapide !
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

