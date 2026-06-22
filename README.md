# 🛡️ Secure D. USB

**Scanner de sécurité USB en temps réel** — détecte les menaces avant qu'elles n'atteignent votre système.

Secure D. USB intercepte chaque clé USB branchée, la gèle en lecture seule, et l'analyse selon 4 niveaux de lecture (signatures évidentes, structure interne, métadonnées, référence externe via VirusTotal) avant d'autoriser tout transfert. Verdict en moins de 10 secondes, sans bloquer votre flux de travail.

---

## ✨ Fonctionnalités

- 🔌 **Interception automatique** — détection du branchement USB (udev / WinAPI) et gel immédiat du transfert
- 🧬 **Mémoire immunitaire locale** — reconnaît les clés déjà analysées via empreintes SHA256, ne réanalyse que ce qui a changé
- 🔍 **Analyse multi-niveaux** — double extension, entropie, chaînes suspectes, métadonnées, scan VirusTotal
- 📊 **Scoring intelligent** — score de suspicion 0-100 avec seuils de décision clairs (sain / suspect / très suspect / malware confirmé)
- ⚡ **Priorisation des fichiers exécutables** — scan immédiat des `.exe .dll .bat .ps1 .vbs ...`, suivi d'un scan complet en arrière-plan
- 🗄️ **Base de données persistante** — historique des 200 dernières clés, registre permanent des clés suspectes
- 🖥️ **Interface claire** — notifications en temps réel, rapport de verdict, tableau de bord, export PDF
- 🌐 **Base communautaire (optionnelle)** — signatures anonymisées partagées entre utilisateurs, conforme RGPD

---

## 🏗️ Architecture


## 🚀 Installation

```bash
git clone https://github.com/<votre-utilisateur>/<nom-du-repo>.git
cd <nom-du-repo>
pip install -r requirements.txt
```

## ▶️ Utilisation

```bash
python main.py
```

> Branchez une clé USB : l'analyse démarre automatiquement.

---

## 🛠️ Stack technique

- **Langage** : Python (lisibilité, écosystème sécurité riche : `hashlib`, `python-magic`, `yara-python`)
- **Base de données** : SQLite (déploiement sans serveur)
- **Interface** : Tkinter (v1.0) → Electron envisagé pour version multiplateforme
- **Référence externe** : API VirusTotal

---

## 🤝 Contribuer

Les contributions sont bienvenues ! Ouvrez une issue ou une pull request pour proposer des améliorations.

## 📄 Licence

À définir.

---

*Projet en développement actif — v1.0 cible Linux en priorité.*
