# 🔭 HYBRID TELESCOPE CONTROL - Guide Complet d'Utilisation

## Version 7.1 - Voice Recognition Enhanced Edition

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#-vue-densemble)
2. [Installation](#-installation)
3. [Premier démarrage](#-premier-démarrage)
4. [Interface principale](#️-interface-principale)
5. [Connexion au télescope](#-connexion-au-télescope-ascom)
6. [Commandes vocales](#-commandes-vocales)
7. [Catalogues d'objets](#-catalogues-dobjets)
8. [Tracking avancé](#-tracking-avancé)
9. [Plate Solving](#-plate-solving)
10. [Filtre de Kalman](#-filtre-de-kalman)
11. [Machine Learning](#-machine-learning-ml)
12. [Météo](#️-intégration-météo)
13. [Sessions](#-gestion-des-sessions)
14. [Résolution de problèmes](#-résolution-de-problèmes)

---

## 🎯 VUE D'ENSEMBLE

**HYBRID Telescope Control** est un logiciel professionnel de contrôle de télescope avec :

| Fonctionnalité | Description |
|----------------|-------------|
| 🎤 **Commandes vocales** | Contrôle vocal en anglais et français avec tolérance aux erreurs |
| 🔭 **ASCOM Alpaca** | Connexion à tout télescope compatible ASCOM |
| 📊 **Tracking avancé** | Filtre de Kalman + Machine Learning pour un suivi précis |
| 🌟 **Plate Solving** | ASTAP (local) + Astrometry.net (en ligne) |
| 📚 **Catalogues complets** | Messier (110), NGC/IC, Étoiles (40+), Planètes (9) |
| 🌤️ **Météo intégrée** | Données en temps réel avec correction de réfraction |

---

## 💿 INSTALLATION

### Prérequis

1. **Windows 10/11** (64-bit)
2. **.NET Framework 4.8** ou supérieur
3. **ASCOM Platform 6.6** ou supérieur (pour le contrôle télescope)
4. **ASTAP** (optionnel, pour le plate solving local)

### Installation

1. Télécharger HYBRID_Telescope_Control_Setup_v7.1.exe
2. Exécuter l'installateur en tant qu'administrateur
3. Suivre les instructions à l'écran
4. L'application sera installée dans C:\Program Files\HYBRID Telescope Control

### Configuration des clés API (optionnel)

Pour utiliser toutes les fonctionnalités :

| Service | Utilisation | Obtenir la clé |
|---------|-------------|----------------|
| **OpenAI** | Commandes vocales avancées | platform.openai.com |
| **Astrometry.net** | Plate solving en ligne | nova.astrometry.net |

---

## 🚀 PREMIER DÉMARRAGE

### 1. Lancer l'application

Double-cliquez sur **HYBRID Telescope Control** depuis le bureau ou le menu Démarrer.

### 2. Configuration initiale

1. Cliquez sur **⚙️ API Credentials** pour configurer vos clés API
2. Entrez votre clé OpenAI pour les commandes vocales avancées
3. Entrez votre clé Astrometry.net pour le plate solving en ligne
4. Cliquez **Test** pour vérifier, puis **Save**

### 3. Connexion au télescope

1. Entrez l'**adresse IP** de votre télescope ASCOM Alpaca (ex: localhost)
2. Entrez le **port** (par défaut: 11111)
3. Cliquez **🔗 Connect**

---

## 🖥️ INTERFACE PRINCIPALE

L'interface est divisée en deux zones principales :

### Panneau Gauche (Contrôles)

- 🔭 HYBRID TELESCOPE CONTROL
- ⚡ ASCOM CONTROL : [IP] [Port] [Connect]
- 📡 Connection Status
- 🎤 Voice Control
- ⏱️ Tracking Duration
- 💬 Activity Log

### Panneau Droit (Onglets)

| Onglet | Icône | Description |
|--------|-------|-------------|
| **Planets** | ☀️ | Système solaire (9 objets) |
| **Messier** | 🌌 | Catalogue Messier M1-M110 |
| **Stars** | ⭐ | 40+ étoiles brillantes |
| **NGC/IC** | 🌠 | Objets du ciel profond |
| **Custom** | 📝 | Objets personnalisés |
| **Session** | 💾 | Historique et statistiques |
| **Wx** | 🌤️ | Météo en temps réel |
| **Tracking** | 🎯 | Tracking avancé + Plate Solving |
| **Help** | ❓ | Aide et documentation |

---

## 🔗 CONNEXION AU TÉLESCOPE (ASCOM)

### Configuration ASCOM Alpaca

1. Assurez-vous que votre télescope est connecté et que le serveur ASCOM Alpaca fonctionne
2. Dans l'application :
   - **Host** : Adresse IP du serveur (ex: 192.168.1.100 ou localhost)
   - **Port** : Port du serveur (défaut: 11111)
3. Cliquez **🔗 Connect**

### États de connexion

| Indicateur | Signification |
|------------|---------------|
| 🟢 **Connected** | Télescope connecté et prêt |
| 🔴 **Disconnected** | Pas de connexion |
| 🟡 **Slewing** | Télescope en mouvement |
| 🟠 **Tracking** | Suivi sidéral actif |
| 🅿️ **Parked** | Télescope garé |

### Commandes de base

| Bouton | Action |
|--------|--------|
| **🔗 Connect** | Connexion au télescope |
| **⛔ Disconnect** | Déconnexion |
| **🅿️ Park** | Garer le télescope |
| **🚗 Unpark** | Dégarer le télescope |
| **📡 Start Tracking** | Démarrer le suivi sidéral |
| **⏹️ Stop Tracking** | Arrêter le suivi |

---

## 🎤 COMMANDES VOCALES

### Configuration

1. Sélectionnez le **moteur de reconnaissance** :
   - **Windows Speech** : Hors-ligne, rapide, précision ~85%
   - **OpenAI ChatGPT + Whisper** : En ligne, très précis (~95%), nécessite clé API

2. Sélectionnez la **langue** :
   - **English (en-US)**
   - **Français (fr-FR)**

3. Cliquez **▶ Start Listening**

### Moteur de reconnaissance robuste

Le moteur vocal est conçu pour être **très tolérant** aux erreurs de prononciation, aux accents et aux phrases mélangeant anglais/français :

- **Fichier CSV phonétique** : un grand fichier (`phonetic_variants_100000.csv`) contient plus de **100 000** variantes :
  - Objets Messier (M1–M110) avec noms anglais et français (« Crab Nebula », « Nébuleuse du Crabe », etc.)
  - Étoiles brillantes (Sirius, Bételgeuse, Vega…) avec prononciations courantes (« Beetlejuice », « Betel juice »)
  - Planètes (« Jupiter », « Jupitère », « Red planet », « Planète rouge »)
  - Objets NGC/IC et surnoms (« Fireworks Galaxy », « Galaxie des feux d’artifice »)
  - Phrases de commande (« go to », « go too », « aller à », « pointer vers », etc.)
- **Fuzzy matching bilingue** :
  - Le texte reconnu est normalisé (minuscules, accents supprimés, chiffres/mots harmonisés)
  - Une distance de Levenshtein est utilisée pour rapprocher ce que vous dites du nom d’objet / commande le plus probable

Résultat : une reconnaissance **très robuste**, même avec un micro moyen et un fort accent.

### Commandes disponibles

#### Navigation (GOTO)

| Anglais | Français | Action |
|---------|----------|--------|
| "Go to M31" | "Aller à M31" | Pointer vers M31 |
| "Point to Jupiter" | "Pointer vers Jupiter" | Pointer vers Jupiter |
| "Find Orion" | "Trouver Orion" | Pointer vers Orion |
| "Show me Vega" | "Montre-moi Véga" | Pointer vers Véga |

#### Contrôle du télescope

| Anglais | Français | Action |
|---------|----------|--------|
| "Park telescope" | "Garer le télescope" | Garer |
| "Start tracking" | "Démarrer le suivi" | Activer le suivi |
| "Stop tracking" | "Arrêter le suivi" | Désactiver le suivi |
| "Connect" | "Connecter" | Connexion ASCOM |

### Tolérance aux erreurs de prononciation

Le système accepte les prononciations approximatives :

| Ce que vous dites | Ce qui est compris |
|-------------------|-------------------|
| "Goat to em thirty one" | goto M31 |
| "Beetlejuice" | Betelgeuse |
| "Jupitère" | Jupiter |
| "M quarante-deux" | M42 |

### Retour vocal et statistiques

Pour chaque **commande vocale effectivement exécutée**, le système fournit :

- Un **retour audio** par synthèse vocale, par exemple :
  - « Going to M31. »
  - « Tracking started. »
  - « M31 is below the horizon. GOTO blocked. »
  - « Mount limits exceeded, command blocked. »
- Des **statistiques en direct** dans le panneau `Voice Control` :
  - Nombre total de commandes reçues
  - Actions réussies
  - Commandes bloquées / invalides (pas de connexion, objet sous l’horizon, limites de monture dépassées…)
  - Erreurs (exceptions ou échecs ASCOM)

Ceci permet de mesurer la performance réelle du système vocal pendant une séance d’observation.

---

## 📚 CATALOGUES D'OBJETS

### ☀️ Planètes (Solar System)

9 objets avec positions calculées en temps réel :
Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune

### 🌌 Messier (M1-M110)

110 objets avec coordonnées fixes :

- **Nébuleuses** : M1 (Crabe), M42 (Orion), M57 (Anneau)...
- **Amas globulaires** : M13 (Hercule), M22...
- **Amas ouverts** : M45 (Pléiades), M44 (Crèche)...
- **Galaxies** : M31 (Andromède), M51 (Tourbillon)...

### ⭐ Étoiles brillantes

40+ étoiles avec magnitude et constellation :
Sirius, Vega, Arcturus, Betelgeuse, etc.

### 🌠 NGC/IC

Objets du ciel profond avec recherche. Le catalogue NGC/IC inclut **de nombreux objets populaires**, par exemple :

- Nébuleuse North America (`NGC7000`), Galaxie Fireworks (`NGC6946`), Nébuleuse California (`NGC1499`)
- Nébuleuse de l’Hélice (`NGC7293`), Nébuleuse de l’Œil de Chat (`NGC6543`), Double amas (`NGC869/NGC884`)
- De nombreuses galaxies / amas célèbres (`NGC2403`, `NGC2683`, `NGC2903`, `NGC4214`, `NGC7331`, etc.)

Tous ces objets sont également inclus dans les **variantes phonétiques** pour la reconnaissance vocale.

### 📝 Objets personnalisés

Ajoutez vos propres objets avec nom, RA et Dec.

---

## 🎯 TRACKING AVANCÉ

Le tracking avancé combine plusieurs technologies pour un suivi précis.

### Workflow

1. **Connecter la caméra** (optionnel)
2. **Démarrer le tracking** : Le système capture des images périodiquement
3. **Plate Solving** : Chaque image est analysée pour déterminer la position exacte
4. **Calcul d'erreur** : Différence entre position attendue et réelle
5. **Filtre de Kalman** : Lisse les mesures et prédit les corrections
6. **Correction** : Ajustement automatique de la monture

---

## 🔍 PLATE SOLVING

Le plate solving détermine la position exacte du télescope en analysant les étoiles.

### Moteurs disponibles

| Moteur | Type | Avantages | Inconvénients |
|--------|------|-----------|---------------|
| **ASTAP** | Local | Rapide (2-10s), hors-ligne | Nécessite installation |
| **Astrometry.net** | En ligne | Pas d'installation | Plus lent (30-120s), internet requis |

---

## 📐 FILTRE DE KALMAN

Le filtre de Kalman est un algorithme mathématique qui améliore la précision du tracking.

Le filtre de Kalman :

- **Prédit** la position future du télescope
- **Corrige** les mesures bruitées du plate solving
- **Lisse** les corrections pour éviter les à-coups
- **S'adapte** au comportement de votre monture

---

## 🤖 MACHINE LEARNING (ML)

Le ML améliore le filtre de Kalman en apprenant le comportement de votre monture.

### Comment ça fonctionne ?

1. **Collecte de données** : Le système enregistre les erreurs de tracking
2. **Entraînement** : Un modèle ML apprend les patterns d'erreur
3. **Prédiction** : Le modèle prédit les erreurs futures
4. **Correction** : Les prédictions améliorent le filtre de Kalman

---

## 🌤️ INTÉGRATION MÉTÉO

Les données météo améliorent la précision (réfraction atmosphérique) et le ML.

Données affichées : Temperature, Humidity, Wind Speed, Cloud Cover, Visibility.

### Profils d’observateur

L’onglet **Météo** permet de définir et sauvegarder différents **profils d’observateur** :

- Exemples de profils :
  - `Home` (jardin / balcon)
  - `Observatory` (observatoire fixe)
- Chaque profil contient :
  - Latitude / Longitude
  - Fuseau horaire
  - Type de monture (pour de futures fonctions avancées)

Le profil actif est utilisé pour :

- La correction de réfraction atmosphérique
- Les vérifications d’**horizon** et de **limites logicielles de monture** avant un GOTO / une commande complexe.

---

## 💾 GESTION DES SESSIONS

### Fonctionnalités

| Fonction | Description |
|----------|-------------|
| **📊 Statistiques** | Objets observés, temps total, erreurs |
| **📝 Notes** | Ajoutez des notes à chaque observation |
| **💾 Sauvegarde** | Exportez vos sessions en JSON |
| **📂 Charger** | Reprenez une session précédente |

---

## 🔧 RÉSOLUTION DE PROBLÈMES

### Le télescope ne se connecte pas

1. Vérifiez que le serveur ASCOM Alpaca fonctionne
2. Vérifiez l'adresse IP et le port

### Les commandes vocales ne fonctionnent pas

1. Vérifiez que le microphone est autorisé
2. Testez avec **🎙️ Test Mic**
3. Pour OpenAI : vérifiez votre clé API

### Le plate solving échoue

1. Vérifiez que ASTAP est installé (pour le mode local)
2. Vérifiez votre connexion internet (pour Astrometry.net)

---

## 📄 LICENCE ET CRÉDITS

**HYBRID Telescope Control** v7.1
© 2025 - Tous droits réservés

### Technologies utilisées

- .NET Framework 4.8
- WPF (Windows Presentation Foundation)
- ASCOM Platform
- OpenAI Whisper & GPT-4o-mini
- ML.NET
- OxyPlot
- NAudio

---

Dernière mise à jour : 28 novembre 2025
