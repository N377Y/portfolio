#!/bin/bash

# Script de vérification du Portfolio
# Marie-Ange KUITCHE

echo "========================================="
echo "🔍 Vérification du Portfolio"
echo "========================================="
echo ""

# 1. Vérification du fichier main.py
echo "1️⃣  Vérification de main.py..."
if python3 -c "from main import portfolio_data; assert 'skills_by_category' in portfolio_data; assert 'profile_image' in portfolio_data" 2>/dev/null; then
    echo "   ✅ main.py est correct"
    echo "   ✓ skills_by_category présent"
    echo "   ✓ profile_image présent"
else
    echo "   ❌ Erreur dans main.py"
    exit 1
fi
echo ""

# 2. Comptage des compétences
echo "2️⃣  Comptage des compétences techniques..."
TOTAL_SKILLS=$(python3 -c "from main import portfolio_data; print(sum(len(skills) for skills in portfolio_data['skills_by_category'].values()))" 2>/dev/null)
echo "   📊 Total: $TOTAL_SKILLS compétences"

python3 << 'EOF'
from main import portfolio_data
for category, skills in portfolio_data['skills_by_category'].items():
    print(f"   • {category}: {len(skills)} compétences")
EOF
echo ""

# 3. Vérification des fichiers
echo "3️⃣  Vérification des fichiers..."
FILES=(
    "templates/index.html"
    "static/css/style.css"
    "static/images/README.md"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file manquant"
    fi
done
echo ""

# 4. Vérification de la photo de profil
echo "4️⃣  Vérification de la photo de profil..."
if [ -f "static/images/profile.jpg" ] || [ -f "static/images/profile.png" ]; then
    echo "   ✅ Photo de profil trouvée"
else
    echo "   ⚠️  Photo de profil manquante"
    echo "   💡 Ajoutez profile.jpg dans static/images/"
    if [ -f "static/images/profile-placeholder.svg" ]; then
        echo "   📋 Placeholder SVG disponible"
    fi
fi
echo ""

# 5. Vérification des compétences du CV
echo "5️⃣  Vérification des compétences du CV..."
REQUIRED_SKILLS=(
    "Python" "Flask" "JavaScript" "React" "Vue.js"
    "C" "C++" "Java" "HTML/CSS" "SQL"
    "Docker" "Kubernetes" "AWS" "PostgreSQL" "MongoDB"
    "VS Code" "PyCharm" "IntelliJ IDEA" "CLion" "Eclipse"
    "JIRA" "Confluence" "GitHub" "Playwright" "JasperSoft" "Xray" "Jam"
)

python3 << 'EOF'
from main import portfolio_data
all_skills = []
for skills in portfolio_data['skills_by_category'].values():
    all_skills.extend([s['name'] for s in skills])

required = ["Python", "Flask", "JavaScript", "React", "Vue.js", "C", "C++", "Java",
            "HTML/CSS", "SQL", "Docker", "Kubernetes", "AWS", "PostgreSQL", "MongoDB",
            "VS Code", "PyCharm", "IntelliJ IDEA", "CLion", "Eclipse",
            "JIRA", "Confluence", "Git/GitHub", "Playwright", "JasperSoft", "Xray", "Jam", "Google Cloud Platform"]

missing = []
for skill in required:
    found = False
    for s in all_skills:
        if skill.lower() in s.lower() or s.lower() in skill.lower():
            found = True
            break
    if not found:
        missing.append(skill)

if missing:
    print("   ⚠️  Compétences manquantes:", ", ".join(missing))
else:
    print("   ✅ Toutes les compétences du CV sont présentes")
EOF
echo ""

# 6. Test de syntaxe Python
echo "6️⃣  Test de syntaxe Python..."
if python3 -m py_compile main.py 2>/dev/null; then
    echo "   ✅ Syntaxe Python correcte"
else
    echo "   ❌ Erreur de syntaxe dans main.py"
fi
echo ""

# 7. Résumé
echo "========================================="
echo "📊 RÉSUMÉ"
echo "========================================="
python3 << 'EOF'
from main import portfolio_data

print(f"👤 Nom: {portfolio_data['name']}")
print(f"💼 Titre: {portfolio_data['title']}")
print(f"🖼️  Photo: {portfolio_data.get('profile_image', 'Non définie')}")
print(f"🎯 Compétences: {sum(len(skills) for skills in portfolio_data['skills_by_category'].values())} au total")
print(f"📂 Catégories: {len(portfolio_data['skills_by_category'])}")
print(f"💼 Expériences: {len(portfolio_data['experiences'])}")
print(f"🎓 Formations: {len(portfolio_data['education'])}")
print(f"📜 Certifications: {len(portfolio_data['certifications'])}")
print(f"🚀 Projets: {len(portfolio_data['projects'])}")
EOF
echo ""

echo "========================================="
echo "✅ Vérification terminée !"
echo "========================================="
echo ""
echo "Pour lancer le portfolio:"
echo "  python main.py"
echo ""
echo "Puis ouvrir dans le navigateur:"
echo "  http://127.0.0.1:5001"
echo ""

