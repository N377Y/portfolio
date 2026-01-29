#!/bin/bash

# Script de démarrage du portfolio

echo "🚀 Démarrage du portfolio..."
echo ""

# Activer l'environnement virtuel
source .venv/bin/activate

# Vérifier que Flask est installé
if ! python -c "import flask" 2>/dev/null; then
    echo "📦 Installation de Flask..."
    pip install -r requirements.txt
fi

echo "✅ Environnement prêt!"
echo "🌐 Démarrage du serveur sur http://localhost:5000"
echo ""
echo "💡 Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

# Lancer l'application
python main.py

