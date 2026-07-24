# 🛡️ Secure D. USB
**Scanner de sécurité USB en temps réel — détecte les menaces avant qu'elles n'atteignent votre système.**

Secure D. USB intercepte chaque clé USB branchée, la protège contre tout transfert non autorisé le temps de l'analyse, et l'examine selon 4 niveaux de lecture (signatures évidentes, structure interne, métadonnées, référence externe via VirusTotal) avant d'autoriser tout transfert. Verdict rapide, sans bloquer durablement votre flux de travail.

## ✨ Fonctionnalités

- 🔌 **Interception automatique** — détection du branchement/débranchement USB (WMI), filtrage par type d'événement
- 🔒 **Isolation de la clé pendant l'analyse** — retrait temporaire de la lettre de lecteur pour empêcher tout transfert humain (Explorateur, AutoPlay) sans bloquer la lecture par le programme lui-même ; réattribution automatique en fin de scan
- 🧬 **Mémoire immunitaire locale** — reconnaît les clés déjà analysées via un identifiant unique et des empreintes SHA256 par fichier, ne réanalyse que ce qui a changé (ajout, modification, déplacement/renommage)
- 🔍 **Analyse multi-niveaux** *(en cours de développement)* — catégorisation par type, entropie, métadonnées, scan VirusTotal ciblé et asynchrone
- 📊 **Scoring intelligent** *(à venir)* — score de suspicion avec seuils de décision clairs
- 🛑 **Procédure d'arrêt sécurisée** — toute interruption (débranchement en cours de scan) est détectée et gérée proprement : pas de plantage, pas de corruption de la mémoire locale (écriture atomique), reprise automatique du cycle
- 🗄️ **Mémoire locale persistante** — pas de dépendance à un serveur central ; conçu pour rester utilisable en environnement isolé (air-gapped)
- 🌐 **Base communautaire** *(vision long terme, non prioritaire pour la v1)* — signatures anonymisées partagées entre utilisateurs

## 🏗️ Architecture

| Module | Rôle | État |
|---|---|---|
| MOD-01 — Intercepteur USB | Détection du branchement/débranchement, inventaire des fichiers | ✅ Terminé et testé |
| MOD-02 — Moteur d'Empreintes | Hashing et reconnaissance des clés connues | ✅ Terminé et testé |
| MOD-03 — Moteur d'Analyse | Analyse 4 niveaux des fichiers | 🚧 En développement |
| MOD-04 — Moteur de Score | Calcul du score et décision proportionnelle | ⏳ À venir |
| MOD-05 — Gestionnaire de Priorités | Ordonnancement du scan, verdict rapide | ⏳ À venir |
| MOD-06 — Base de Données | Historique et signatures locales | ⏳ À venir |
| MOD-07 — Interface Utilisateur | Notifications, rapports, dashboard | ⏳ À venir |
| MOD-08 — Base Communautaire | Synchronisation des signatures entre utilisateurs | ⏳ À venir |
| MOD-09 — Intégrité | Protection du volume pendant l'analyse (isolation, réattribution) | ✅ Terminé et testé |

## 🚀 Installation

```
git clone https://github.com/<williamnseke69-droid>/<Secure-D-USB>.git
cd <Secure-D-USB>
pip install -r requirements.txt
```

Nécessite des droits administrateur (protection du volume, gestion des lettres de lecteur).

## ▶️ Utilisation

```
python main.py
```

Branchez une clé USB : l'analyse démarre automatiquement. Le programme tourne en continu et reprend son attente après chaque cycle, y compris après une interruption imprévue.

## 🛠️ Stack technique

- **Langage** : Python
- **Interaction système bas niveau (Windows)** : `wmi` (détection d'événements de volume), `pywin32` (`win32file` — gestion des lettres de lecteur et des volumes)
- **Base de données** : JSON local pour la v1 (mémoire d'empreintes), SQLite envisagé pour l'historique (MOD-06)
- **Interface** : à définir (Tkinter envisagé pour une v1 en ligne de commande/desktop minimal)
- **Référence externe** : API VirusTotal (usage ciblé et asynchrone, pas systématique)

## 🤝 Contribuer

Les contributions sont bienvenues ! Ouvrez une issue ou une pull request pour proposer des améliorations.

## 📄 Licence

À définir.

---

Projet en développement actif — **v1.0 cible Windows en priorité** (choix fait après plusieurs jours de développement initial sur Linux, pour pouvoir tester directement en conditions réelles).
