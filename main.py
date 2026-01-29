"""
Portfolio Web Application
A Flask-based portfolio website showcasing skills, projects, and professional experience.
Author: Marie-Ange KUITCHE
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Application configuration
app.config['SECRET_KEY'] = 'dev-portfolio-secret-key-2026'

# Portfolio data structure containing all personal and professional information
portfolio_data = {
    'name': 'Marie-Ange KUITCHE',
    'title': 'Développeuse Full Stack | QA & Test Automation',
    'bio': 'Développeuse Full Stack spécialisée QA & Test Automation avec passion pour l\'IA et les architectures cloud-natives. J\'allie expertise en test automation (ISTQB Advanced Certified) et développement logiciel pour créer des solutions robustes et sécurisées.',
    'profile_image': 'static/images/profile.png',  # Photo de profil
    'skills_by_category': {
        'programming': [
            {'name': 'Python', 'level': 95, 'icon': 'fab fa-python'},
            {'name': 'JavaScript', 'level': 90, 'icon': 'fab fa-js'},
            {'name': 'Java', 'level': 80, 'icon': 'fab fa-java'},
            {'name': 'C', 'level': 80, 'icon': 'fas fa-code'},
            {'name': 'C++', 'level': 80, 'icon': 'fas fa-code'},
            {'name': 'HTML/CSS', 'level': 95, 'icon': 'fab fa-html5'},
            {'name': 'SQL', 'level': 85, 'icon': 'fas fa-database'},
        ],
        'frameworks': [
            {'name': 'Flask', 'level': 95, 'icon': 'fas fa-flask'},
            {'name': 'React', 'level': 75, 'icon': 'fab fa-react'},
            {'name': 'Vue.js', 'level': 75, 'icon': 'fab fa-vuejs'}
        ],
        'devops_cloud': [
            {'name': 'Docker', 'level': 85, 'icon': 'fab fa-docker'},
            {'name': 'Kubernetes', 'level': 30, 'icon': 'fas fa-dharmachakra'},
            {'name': 'AWS', 'level': 60, 'icon': 'fab fa-aws'},
            {'name': 'Google Cloud Platform', 'level': 70, 'icon': 'fab fa-google'},
        ],
        'tools_ide': [
            {'name': 'VS Code', 'level': 95, 'icon': 'fas fa-code'},
            {'name': 'PyCharm', 'level': 90, 'icon': 'fas fa-code'},
            {'name': 'IntelliJ IDEA', 'level': 85, 'icon': 'fas fa-code'},
            {'name': 'CLion', 'level': 80, 'icon': 'fas fa-code'},
            {'name': 'Eclipse', 'level': 75, 'icon': 'fas fa-code'},
            {'name': 'Git/GitHub', 'level': 90, 'icon': 'fab fa-github'},
            {'name': 'JIRA', 'level': 90, 'icon': 'fab fa-jira'},
            {'name': 'Confluence', 'level': 65, 'icon': 'fab fa-confluence'},
        ],
        'testing_qa': [
            {'name': 'Playwright', 'level': 75, 'icon': 'fas fa-robot'},
            {'name': 'JasperSoft', 'level': 65, 'icon': 'fas fa-chart-bar'},
            {'name': 'Xray', 'level': 75, 'icon': 'fas fa-vial'},
            {'name': 'Jam', 'level': 65, 'icon': 'fas fa-bug'},
        ],
        'databases': [
            {'name': 'PostgreSQL', 'level': 85, 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'level': 50, 'icon': 'fas fa-database'},
            {'name': 'NoSQL', 'level': 50, 'icon': 'fas fa-database'},
        ],
        'ai_coding_tools': [
            {'name': 'Claude Code', 'level': 90, 'icon': 'fas fa-robot'},
            {'name': 'GitHub Copilot', 'level': 95, 'icon': 'fab fa-github'},
            {'name': 'Manus', 'level': 85, 'icon': 'fas fa-hand-sparkles'},
            {'name': 'Gemini', 'level': 80, 'icon': 'fas fa-gem'},
            {'name': 'GPT Codex', 'level': 85, 'icon': 'fas fa-brain'},
        ],
    },
    # Compatibilité avec l'ancien format (garde les skills combinées pour les sections qui l'utilisent)
    'skills': [
        {'name': 'Python', 'level': 95, 'icon': 'fab fa-python'},
        {'name': 'JavaScript', 'level': 90, 'icon': 'fab fa-js'},
        {'name': 'React', 'level': 75, 'icon': 'fab fa-react'},
        {'name': 'Flask', 'level': 95, 'icon': 'fas fa-flask'},
        {'name': 'Docker', 'level': 85, 'icon': 'fab fa-docker'},
    ],
    'soft_skills': [
        {
            'name': 'Écoute active',
            'icon': 'fas fa-ear-listen',
            'description': 'Capacité d\'écoute attentive pour comprendre les besoins et les attentes des clients et équipes.'
        },
        {
            'name': 'Curiosité',
            'icon': 'fas fa-lightbulb',
            'description': 'Soif d\'apprendre et de découvrir de nouvelles technologies et approches innovantes.'
        },
        {
            'name': 'Résilience',
            'icon': 'fas fa-shield-alt',
            'description': 'Capacité à persévérer face aux défis et à rebondir après les obstacles.'
        },
        {
            'name': 'Créativité',
            'icon': 'fas fa-palette',
            'description': 'Approche créative pour résoudre des problèmes complexes avec des solutions innovantes.'
        },
        {
            'name': 'Intelligence émotionnelle',
            'icon': 'fas fa-heart',
            'description': 'Compréhension et gestion des émotions pour favoriser de bonnes relations de travail.'
        },
        {
            'name': 'Flexibilité et adaptabilité',
            'icon': 'fas fa-sync-alt',
            'description': 'Adaptation rapide aux changements et aux nouvelles situations professionnelles.'
        },
    ],
    'languages': [
        {
            'name': 'Français',
            'level': 'Natif',
            'icon': 'fas fa-language'
        },
        {
            'name': 'Anglais',
            'level': 'Niveau C2',
            'icon': 'fas fa-language'
        },
    ],
    'experiences': [
        {
            'title': 'Consultante Testing',
            'company': 'Haulogy, Poitiers',
            'period': 'Novembre 2023 - Présent',
            'icon': 'fas fa-briefcase',
            'description': 'Tests et automatisation pour améliorer la qualité logicielle des applications clients.',
            'achievements': [
                'Tests Fonctionnels E2E : Conception et exécution de cas de test fonctionnels, validation règles métier. Couverture : 89% des fonctionnalités critiques',
                'Support Client & Ticketing JIRA : Gestion tickets utilisateurs, triage, suivi et documentation. Métrique : 94% tickets remontés en SLA (<48h)',
                'Reporting BO (Jaspersoft & SQL) : Création rapports métier (SQL queries complexes), dashboards Jaspersoft. Impact : Réduction temps reporting manuel de 50%',
                'Cookbooks de paramétrage : Documentation technique complète pour configuration système, onboarding équipes. Utilisation : 60% des nouvelles configurations l\'utilisent (source truth)'
            ]
        },
        {
            'title': 'Stagiaire en développement Frontend',
            'company': 'Clarans Afrique, Douala (Afrique CA)',
            'period': 'Juin 2022 - Août 2022',
            'icon': 'fas fa-code',
            'description': 'Apprentissage du développement front-end et création d\'applications web interactives.',
            'achievements': [
                'Apprentissage du développement front-end, programmation en JavaScript',
                'Création d\'une application web interactive en utilisant du HTML/CSS et JavaScript'
            ]
        },
    ],
    'education': [
        {
            'degree': 'Ingénieur Développement Logiciel - Test et Qualité',
            'school': 'École supérieure d\'ingénieurs en génie électrique, France',
            'period': 'Septembre 2023 - Présent',
            'icon': 'fas fa-graduation-cap',
            'description': 'Analyse et conception : Algorithmique et structures, UML et Design Pattern, SQL et NoSQL. Développement logiciel, Architecture et Test : DevOps, POO, TDD et qualité. Qualité logicielle : Assurance, performance et stabilité. Architecture des SI et Cybersécurité. Cloud & DevOps : Programmation système et Infrastructure As a Code, Déploiement et Cloud Computing. Certifications : ISTQB et Numérique Responsable. Management et suivi de projet.'
        },
        {
            'degree': 'Prépa Intégrée en Ingénierie Générale',
            'school': 'Prepavogt, Yaoundé, Cameroun',
            'period': 'Septembre 2021 - Juin 2023',
            'icon': 'fas fa-university',
            'description': 'Formation préparatoire en ingénierie avec fondamentaux scientifiques et techniques.'
        },
    ],
    'certifications': [
        {
            'name': 'ISTQB Certified Tester Advanced Level Test Automation Engineering',
            'issuer': 'ISTQB - International Software Testing Qualifications Board',
            'icon': 'fas fa-certificate',
            'description': 'Certification avancée en automatisation des tests et ingénierie de la qualité logicielle.',
            'credential_id': None,
            'link': 'static/certifications/ISTQB.pdf',
            'pdf_file': 'static/certifications/ISTQB.pdf'
        },
        {
            'name': 'Google Cloud Digital Leader',
            'issuer': 'Google Cloud',
            'icon': 'fab fa-google',
            'description': 'Certification sur les fondamentaux du cloud computing et des services Google Cloud.',
            'credential_id': None,
            'link': 'static/certifications/CloudDigitalLeader.pdf',
            'pdf_file': 'static/certifications/CloudDigitalLeader.pdf'
        },
        {
            'name': 'Numérique Responsable',
            'issuer': 'Institut du Numérique Responsable',
            'icon': 'fas fa-leaf',
            'description': 'Certification sur les bonnes pratiques du numérique responsable et durable.',
            'credential_id': None,
            'link': 'static/certifications/Numerique-responsable.pdf',
            'pdf_file': 'static/certifications/Numerique-responsable.pdf'
        },
    ],
    'activities': [
        # Les activités et hackathons peuvent être ajoutés ici si nécessaire
    ],
    'hobbies': [
        {
            'name': 'Sport',
            'description': 'Volleyball, Tennis de table, Danse de salon',
            'icon': 'fas fa-volleyball-ball'
        },
        {
            'name': 'Musique',
            'description': 'Gagnante Nationale Turkish Joyful Litterary',
            'icon': 'fas fa-music'
        },
        {
            'name': 'Lecture',
            'description': 'Manga, littérature anglaise',
            'icon': 'fas fa-book'
        },
        {
            'name': 'Écriture',
            'description': 'Participation Queen\'s Commonwealth Essay Competition',
            'icon': 'fas fa-pen-fancy'
        },
    ],
    'references': [
        {
            'name': 'Ahlem Benabderrahmane',
            'title': 'Enseignante chercheuse en électronique',
            'organization': 'ESIGELEC',
            'email': 'Ahlem.Benabderrahmane@esigelec.fr'
        },
        {
            'name': 'Georges El Chidiac',
            'title': 'Chef de projet technology',
            'organization': 'Haulogy',
            'email': 'georges.elchidiac@haulogy.net'
        },
    ],
    'projects': [
        {
            'title': 'HackAtassa - Plateforme de gestion de Hackathons',
            'description': 'Plateforme complète pour organiser et gérer des hackathons : inscriptions, gestion des équipes, soumissions de projets, évaluations et classements. Interface intuitive pour organisateurs et participants.',
            'tech': ['Python', 'Flask', 'React', 'PostgreSQL', 'WebSockets'],
            'color': '#667eea',
            'image': 'static/projets/HackAtassa.png',
            'github': '#',
            'demo': '#',
            'details': {
                'objectif': 'Créer une plateforme end-to-end pour faciliter l\'organisation et la participation aux hackathons, de l\'inscription jusqu\'au classement final.',
                'features': [
                    'Système d\'inscription avec validation automatique',
                    'Formation automatique des équipes selon les compétences',
                    'Soumission de projets avec upload de fichiers',
                    'Système d\'évaluation par jury avec critères personnalisables',
                    'Classement en temps réel avec WebSockets',
                    'Dashboard administrateur pour suivi complet'
                ],
                'challenges': [
                    'Gestion des communications temps réel entre 100+ participants simultanés',
                    'Optimisation des requêtes PostgreSQL pour le classement dynamique',
                    'Architecture scalable pour supporter plusieurs hackathons en parallèle'
                ],
                'results': 'Utilisé avec succès pour 3 hackathons (200+ participants). Réduction de 70% du temps de gestion administrative.'
            }
        },
        {
            'title': 'Footelly - Suivi de matchs de Babyfoot',
            'description': 'Application web de suivi en temps réel de matchs de babyfoot avec gestion des scores, statistiques des joueurs, classements et historique des parties. Interface responsive et temps réel.',
            'tech': ['Python', 'Flask', 'JavaScript', 'SQLite', 'Chart.js'],
            'color': '#f093fb',
            'image': 'static/projets/footelly.png',
            # Ajoute ici ton vrai repo si dispo : le bouton "Voir le code" servira de fallback si Render est en veille.
            'github': '#',
            # Render peut être lent au premier chargement (cold start) : le lien fonctionne mais peut prendre 10-30s.
            'demo': 'https://footelly.onrender.com/',
            'details': {
                'objectif': 'Digitaliser et gamifier les matchs de babyfoot en entreprise avec statistiques détaillées et classements compétitifs.',
                'features': [
                    'Enregistrement des matchs en direct avec chronomètre intégré',
                    'Calcul automatique du classement ELO des joueurs',
                    'Statistiques personnelles : ratio victoires/défaites, évolution du score',
                    'Graphiques interactifs avec Chart.js (performances dans le temps)',
                    'Historique complet des parties avec replay détaillé',
                    'Mode tournoi avec brackets et élimination directe'
                ],
                'challenges': [
                    'Optimisation de l\'interface pour saisie rapide des scores pendant les matchs',
                    'Algorithme ELO adapté au babyfoot (équipes variables)',
                    'Responsive design pour utilisation sur tablette en bord de table'
                ],
                'results': 'Déployé en production, utilisé quotidiennement par 50+ joueurs. Augmentation de 40% de l\'engagement des employés.'
            }
        },
        {
            'title': 'Système PACS IA pour Clinique IRM',
            'description': 'Conception d\'un logiciel open-source inspiré syngo.via/PACS : archivage DICOM, visualisation 3D IRM, IA pour détection anomalies (rapports pré-remplis). Stack : Python (FastAPI/Flask), ML (TensorFlow/MONAI pour IA image), MongoDB (métadonnées), Frontend React.',
            'tech': ['Python', 'FastAPI', 'Flask', 'TensorFlow', 'MONAI', 'MongoDB', 'React'],
            'color': '#4facfe',
            'image': None,
            'github': '#',
            'demo': '#',
            'details': {
                'objectif': 'Développer une solution PACS open-source avec IA intégrée pour détecter automatiquement les anomalies sur les IRM cérébrales.',
                'features': [
                    'Import et parsing de fichiers DICOM (images médicales)',
                    'Visualisation 3D interactive des IRM avec reconstruction volumétrique',
                    'Modèle IA (CNN avec MONAI) pour détection tumeurs cérébrales',
                    'Génération automatique de rapports pré-remplis pour radiologues',
                    'Archivage sécurisé avec MongoDB et chiffrement des données patient',
                    'Interface web React pour consultation multi-plateforme'
                ],
                'challenges': [
                    'Traitement d\'images DICOM volumineuses (500+ MB par scan)',
                    'Entraînement du modèle IA avec dataset limité (augmentation de données)',
                    'Conformité RGPD et sécurisation des données médicales sensibles',
                    'Optimisation du rendu 3D pour fluidité dans le navigateur'
                ],
                'results': 'Prototype fonctionnel avec 85% de précision sur la détection. Réduction estimée de 30% du temps d\'analyse radiologique.'
            }
        },
        {
            'title': 'Plateforme d\'onboarding professionnel',
            'description': 'Développement d\'une plateforme web d\'intégration pour nouveaux employés: formations sur le métier et sur les logiciels natifs. Stack : Python/Flask, React, PostgreSQL. API REST pour synchronisation RH.',
            'tech': ['Python', 'Flask', 'React', 'PostgreSQL', 'REST API'],
            'color': '#43e97b',
            'image': None,
            'github': '#',
            'demo': '#',
            'details': {
                'objectif': 'Automatiser et standardiser le processus d\'intégration des nouveaux employés avec parcours personnalisés.',
                'features': [
                    'Parcours d\'onboarding personnalisés selon le poste',
                    'Modules de formation interactifs (vidéos, quiz, exercices)',
                    'Suivi de progression en temps réel pour RH et managers',
                    'Synchronisation automatique avec le SIRH via API REST',
                    'Attribution automatique des accès et licences logicielles',
                    'Dashboard analytics pour optimiser les parcours'
                ],
                'challenges': [
                    'Intégration avec système RH legacy (API SOAP vers REST)',
                    'Gestion de contenu multimedia lourd (compression, CDN)',
                    'Personnalisation dynamique selon 50+ profils de poste différents'
                ],
                'results': 'Réduction de 60% du temps d\'onboarding (de 2 semaines à 5 jours). Taux de satisfaction de 92%.'
            }
        },
        {
            'title': 'Projet d\'automatisation des Tests avec Playwright',
            'description': 'Conception et implémentation suite de tests automatisés (Playwright) pour tests fonctionnels. Gestion qualité : rapports détaillés, identification anomalies, création automatique de tickets interne.',
            'tech': ['Playwright', 'JavaScript', 'TypeScript', 'Testing'],
            'color': '#667eea',
            'image': None,
            'github': '#',
            'demo': '#',
            'details': {
                'objectif': 'Mettre en place une suite de tests E2E automatisée pour garantir la qualité et réduire les régressions.',
                'features': [
                    'Suite de 200+ tests automatisés couvrant parcours critiques',
                    'Tests cross-browser (Chrome, Firefox, Safari, Edge)',
                    'Tests responsive sur différentes résolutions',
                    'Rapports HTML détaillés avec screenshots et vidéos des échecs',
                    'Intégration CI/CD avec GitLab (déclenchement automatique)',
                    'Création automatique de tickets Jira pour bugs détectés'
                ],
                'challenges': [
                    'Gestion des tests asynchrones et des temps d\'attente dynamiques',
                    'Stabilisation des tests flaky (taux de fiabilité > 98%)',
                    'Optimisation parallélisation pour réduire temps exécution (30 min → 8 min)',
                    'Maintenance de la suite avec évolutions fréquentes de l\'application'
                ],
                'results': 'Détection de 45+ bugs critiques avant production. Couverture de tests passée de 30% à 85%. ROI de 3 mois.'
            }
        },
        {
            'title': 'Outil de gestion administrative pour PME',
            'description': 'Développement d\'une plateforme complète pour automatiser déclarations administratives (fiscales, sociales, RH, conformité) et veille réglementaire. Stack : Python/Flask, TypeScript/React, Firestore, Docker, GCP.',
            'tech': ['Python', 'Flask', 'TypeScript', 'React', 'Firestore', 'Docker', 'GCP'],
            'color': '#f093fb',
            'image': None,
            'github': '#',
            'demo': '#',
            'details': {
                'objectif': 'Simplifier la gestion administrative des PME en automatisant les déclarations obligatoires et la veille réglementaire.',
                'features': [
                    'Automatisation des déclarations fiscales (TVA, IS, CFE)',
                    'Gestion RH : déclarations sociales, DSN, contrats',
                    'Veille réglementaire avec alertes sur changements législatifs',
                    'Génération automatique de documents conformes',
                    'Tableau de bord avec rappels et échéances',
                    'Export comptable vers logiciels tiers (Sage, Cegid)'
                ],
                'challenges': [
                    'Adaptation aux évolutions législatives fréquentes',
                    'Gestion de la complexité réglementaire (200+ types de déclarations)',
                    'Sécurisation maximale (données financières sensibles)',
                    'Architecture multi-tenant pour servir 100+ PME simultanément'
                ],
                'results': 'Plateforme utilisée par 35 PME. Réduction de 80% du temps administratif. Zéro erreur de déclaration sur 6 mois.'
            }
        }
    ],
    'contact': {
        'email': 'marie-ange.kuitche@groupe-esigelec.org',
        'phone': '+33 7 68 12 65 86',
        'location': 'Poitiers (86000), France',
        'github': 'https://github.com/N377Y',
        'linkedin': 'https://www.linkedin.com/in/marie-ange-nelly-kuitche-megouo-a49974226/'
    }
}

# Routes
@app.route('/')
def index():
    """Render the main portfolio page"""
    return render_template('index.html', data=portfolio_data)

@app.route('/api/data')
def get_data():
    """API endpoint to get portfolio data as JSON"""
    return jsonify(portfolio_data)

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, port=5003)
