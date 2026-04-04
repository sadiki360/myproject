# 🎓 PreSkool — Système de Gestion Scolaire

<div align="center">

![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14.3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

**Application web de gestion scolaire complète — Architecture MVT Django**

*Projet de Fin de Module | Développement Web Avancé — Back End Python | FST Tanger 2025/2026*

</div>

---

## 🎬 Démonstration Vidéo

<div align="center">

https://github.com/user-attachments/assets/141d85c5-f652-4626-a224-58095def3c2b

</div>

---

## 👥 Équipe

| Champ | Détail |
|-------|--------|
| 👩‍💻 Développeuse | Maroua Sadiki — N° Apogée : 24012821 |
| 👩‍💻 Binôme | Salma Samah |
| 👩‍🏫 Professeur | Prof. Sara AHSAIN |
| 🏫 Établissement | Faculté des Sciences et Techniques de Tanger |

---

## 📋 Description

**PreSkool** est une application web de gestion scolaire développée avec le framework **Django (Python)**. Elle centralise la gestion des étudiants, enseignants, départements, matières, examens et congés dans une interface moderne et sécurisée, avec un système de contrôle d'accès basé sur les rôles.

---

## ✨ Fonctionnalités

| Module | Fonctionnalités |
|--------|----------------|
| 🔐 **Authentification** | Login / Logout / Signup · 3 rôles (Admin, Enseignant, Étudiant) |
| 👨‍🎓 **Étudiants** | CRUD complet · Profil avec photo · Gestion des parents |
| 👨‍🏫 **Enseignants** | CRUD complet · Profil avec photo · Filtres par spécialité |
| 🏢 **Départements** | CRUD · Chef de département assigné |
| 📚 **Matières** | CRUD · Lien département + enseignant |
| 🗓️ **Congés** | Calendrier des jours fériés |
| 📝 **Examens** | Planification · Saisie et consultation des résultats |
| 📊 **Dashboard** | Statistiques en temps réel |
| 🕐 **Emploi du Temps** | Affichage visuel par groupe et session *(BONUS +5pts)* |

---

## 🛠️ Technologies Utilisées

- **Python 3.14.3**
- **Django 6.0.3**
- **SQLite** (base de données)
- **Bootstrap** (template PreSkool)
- **Pillow** (gestion des images)
- **Git / GitHub** (versioning)

---

## 🚀 Installation et Lancement

### Prérequis
- Python 3.10+ installé
- Git installé

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/sadiki360/myproject.git
cd myproject

# 2. Créer et activer l'environnement virtuel
python -m venv venv

# Sur Windows :
venv\Scripts\activate

# Sur Linux / Mac :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 5. Créer un superutilisateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

L'application est accessible sur : **http://127.0.0.1:8000/**

---

## 🔑 Comptes de Test

| Username | Password | Rôle | Accès |
|----------|----------|------|-------|
| `admin_test` | `admin123` | Administrateur | Accès complet |
| `teacher_test` | `teacher123` | Enseignant | Examens + Résultats |
| `student_test` | `student123` | Étudiant | Lecture seule |

> ⚠️ Le compte superutilisateur (`admin_maroua`) est créé manuellement via `createsuperuser`.

---

## 🗂️ Structure du Projet

```
school/
├── school/              # Configuration principale (settings.py, urls.py)
├── faculty/             # Dashboard et accueil
├── student/             # Gestion des étudiants (Student, Parent)
├── home_auth/           # Authentification (CustomUser)
├── teacher/             # Gestion des enseignants
├── department/          # Gestion des départements
├── subject/             # Gestion des matières
├── holiday/             # Gestion des congés
├── exam/                # Examens et résultats
├── timetable/           # Emploi du temps (BONUS)
├── static/assets/       # CSS, JS, Images Bootstrap
├── templates/           # Templates HTML
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 🔒 Sécurité et Rôles

Les vues sont protégées par des décorateurs personnalisés :

```python
@login_required      # Tous les utilisateurs connectés
@admin_required      # Administrateurs uniquement
@teacher_required    # Enseignants + Administrateurs
```

| Vue | Accès |
|-----|-------|
| Dashboard, Emploi du temps | `@login_required` |
| Ajouter examens / résultats | `@teacher_required` |
| Toutes les opérations CRUD | `@admin_required` |

---

## 🗃️ Modèles et Relations

```
CustomUser (AbstractUser)
    └── is_student | is_teacher | is_admin

Student ──(OneToOne)──► Parent
Department ──(ForeignKey)──► Teacher (chef)
Subject ──(ForeignKey)──► Teacher
Subject ──(ForeignKey)──► Department
Exam ──(ForeignKey)──► Subject
ExamResult ──(ForeignKey)──► Exam + Student
```

---

## 🕐 Emploi du Temps (BONUS)

Accessible via `/timetable/` — affichage par jour et session :

| Jour | Matin (08:30–12:30) | Soir (14:00–18:00) |
|------|---------------------|---------------------|
| Lundi | AD-S1/S2 : Analyse 3 | IDAI-S1/S2 : UML |
| Mardi | AD-S1/S2 : Python | IDAI-S1/S2 : Soft Skills |
| Mercredi | AD-S1/S2 : HTML/CSS | IDAI-S1/S2 : Analyse 3 |
| Jeudi | AD-S1/S2 : Soft Skills | IDAI-S1/S2 : Python |
| Vendredi | AD-S1/S2 : Révision | IDAI-S1/S2 : TP |

---

## 🖥️ Interface Admin Django

Accessible via **http://127.0.0.1:8000/admin/** avec les identifiants superutilisateur.

Toutes les applications sont enregistrées avec filtres et recherche configurés.

---

## 📦 Dépendances (requirements.txt)

```
django==6.0.3
pillow
```

Pour régénérer : `pip freeze > requirements.txt`

---

## 📄 Licence

Projet académique réalisé dans le cadre du module **Développement Web Avancé — Back End Python**.  
Faculté des Sciences et Techniques de Tanger — Université Abdelmalek Essaadi — 2025/2026.

---

<div align="center">
  Made with ❤️ by <strong>Maroua Sadiki</strong> & <strong>Salma Samah</strong>
</div>
