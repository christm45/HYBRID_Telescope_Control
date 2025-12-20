# 🔭 HYBRID TELESCOPE CONTROL - Complete User Guide

## Version 7.3 - Local AI Edition

---

## 📋 TABLE OF CONTENTS

1. [Overview](#-overview)
2. [Installation](#-installation)
3. [First Launch](#-first-launch)
4. [Main Interface](#-main-interface)
5. [Telescope Connection](#-telescope-connection-ascom)
6. [Voice Commands](#-voice-commands)
7. [Object Catalogs](#-object-catalogs)
8. [Advanced Tracking](#-advanced-tracking)
9. [Plate Solving](#-plate-solving)
10. [Kalman Filter](#-kalman-filter)
11. [Machine Learning](#-machine-learning-ml)
12. [Weather](#-weather-integration)
13. [Sessions](#-session-management)
14. [Troubleshooting](#-troubleshooting)

---

## 🎯 OVERVIEW

**HYBRID Telescope Control** is a professional telescope control software with:

| Feature | Description |
|---------|-------------|
| 🎤 **Voice Commands** | 100% local AI (Whisper Local + Ollama) or cloud (OpenAI), English and French |
| 🔭 **ASCOM Alpaca** | Connection to any ASCOM-compatible telescope |
| 📊 **Advanced Tracking** | Kalman Filter + Machine Learning for precise tracking |
| 🌟 **Plate Solving** | ASTAP (local) + Astrometry.net (online) |
| 📚 **Complete Catalogs** | Unified catalog with Messier, NGC/IC, Stars, Planets |
| 🌤️ **Integrated Weather** | Real-time data with refraction correction |
| 🤖 **Local AI** | Ollama + Mistral 3 for offline voice recognition |
| 🎯 **Fine-Tuning** | 200k+ examples, 20k audio files for Whisper Local training |

---

## 💿 INSTALLATION

### Prerequisites

1. **Windows 10/11** (64-bit)
2. **.NET Framework 4.8** or higher
3. **ASCOM Platform 6.6** or higher (for telescope control)
4. **ASTAP** (optional, for local plate solving)

### Installation

1. Download HYBRID_Telescope_Control_Setup_v7.1.exe
2. Run the installer as administrator
3. Follow the on-screen instructions
4. The application will be installed in C:\Program Files\HYBRID Telescope Control

### Voice Recognition Engines

The application supports **three voice recognition engines**:

| Engine | Type | Cost | Internet | Accuracy |
|--------|------|------|----------|----------|
| **Whisper Local** | Local | Free | No | 90-95% |
| **Ollama + Mistral** | Local | Free | No | 85-90% |
| **OpenAI Whisper + GPT** | Cloud | ~€0.10/hr | Yes | 95%+ |
| **Windows Speech** | Built-in | Free | No | 70-85% |

**Recommended**: Whisper Local (100% local, no API limits, fine-tuned with 200k+ examples)

### API Key Configuration (optional)

For cloud-based features:

| Service | Usage | Get Key |
|---------|-------|---------|
| **OpenAI** | Cloud voice commands (optional) | platform.openai.com |
| **Astrometry.net** | Online plate solving | nova.astrometry.net |

---

## 🚀 FIRST LAUNCH

### 1. Launch the Application

Double-click on **HYBRID Telescope Control** from the desktop or Start menu.

### 2. Initial Configuration

1. Click on **⚙️ API Credentials** to configure your API keys
2. Enter your OpenAI key for advanced voice commands
3. Enter your Astrometry.net key for online plate solving
4. Click **Test** to verify, then **Save**

### 3. Telescope Connection

1. Enter the **IP address** of your ASCOM Alpaca telescope (e.g.: localhost)
2. Enter the **port** (default: 11111)
3. Click **🔗 Connect**

---

## 🖥️ MAIN INTERFACE

The interface is divided into two main areas:

### Left Panel (Controls)

- 🔭 HYBRID TELESCOPE CONTROL
- ⚡ ASCOM CONTROL: [IP] [Port] [Connect]
- 📡 Connection Status
- 🎤 Voice Control
- ⏱️ Tracking Duration
- 💬 Activity Log

### Right Panel (Tabs)

| Tab | Icon | Description |
|-----|------|-------------|
| **Planets** | ☀️ | Solar system (9 objects) |
| **Messier** | 🌌 | Messier catalog M1-M110 |
| **Stars** | ⭐ | 40+ bright stars |
| **NGC/IC** | 🌠 | Deep sky objects |
| **Custom** | 📝 | Custom objects |
| **Session** | 💾 | History and statistics |
| **Wx** | 🌤️ | Real-time weather |
| **Tracking** | �� | Advanced tracking + Plate Solving |
| **Help** | ❓ | Help and documentation |

---

## 🔗 TELESCOPE CONNECTION (ASCOM)

### ASCOM Alpaca Configuration

1. Make sure your telescope is connected and the ASCOM Alpaca server is running
2. In the application:
   - **Host**: Server IP address (e.g.: 192.168.1.100 or localhost)
   - **Port**: Server port (default: 11111)
3. Click **🔗 Connect**

### Connection States

| Indicator | Meaning |
|-----------|---------|
| 🟢 **Connected** | Telescope connected and ready |
| 🔴 **Disconnected** | No connection |
| 🟡 **Slewing** | Telescope moving |
| 🟠 **Tracking** | Sidereal tracking active |
| 🅿️ **Parked** | Telescope parked |

### Basic Commands

| Button | Action |
|--------|--------|
| **🔗 Connect** | Connect to telescope |
| **⛔ Disconnect** | Disconnect |
| **🅿️ Park** | Park telescope |
| **🚗 Unpark** | Unpark telescope |
| **📡 Start Tracking** | Start sidereal tracking |
| **⏹️ Stop Tracking** | Stop tracking |

---

## 🎤 VOICE COMMANDS

### Configuration

1. Select the **recognition engine**:
   - **Whisper Local** ⭐ (Recommended): 100% local, fine-tuned with 200k+ examples, no API limits
   - **Ollama Local AI**: 100% local, Mistral 3, free and unlimited
   - **OpenAI ChatGPT + Whisper**: Cloud-based, very accurate (~95%), requires API key
   - **Windows Speech**: Built-in Windows, offline, ~70-85% accuracy

2. Select the **language**:
   - **English (en-US)**
   - **Français (fr-FR)**

3. Click **▶ Start Listening**

**Note**: Whisper Local uses a fine-tuned model trained on 20,000 audio files (10k EN + 10k FR) for optimal astronomy command recognition.

### Robust Recognition Engine

The voice engine is designed to be **extremely tolerant** to pronunciation errors, accents, and mixed English/French sentences:

- **Fine-tuned Whisper Local model**: Trained on **20,000 audio files** (10,000 EN + 10,000 FR commands) for astronomy-specific recognition
- **Phonetic variants CSV**: Contains more than **200,000** variants:
  - Messier objects (M1–M110) with English and French names ("Crab Nebula", "Nébuleuse du Crabe", etc.)
  - Bright stars (Sirius, Betelgeuse, Vega…) with common mispronunciations ("Beetlejuice", "Betel juice")
  - Planets ("Jupiter", "Jupitère", "Red planet", "Planète rouge")
  - NGC/IC objects and their nicknames ("Fireworks Galaxy", "Galaxie des feux d'artifice")
  - Command phrases ("go to", "go too", "aller à", "pointer vers", etc.)
- **Bilingual fuzzy matching**:
  - All recognized text is normalized (lowercased, accents removed, digits/words harmonized)
  - A fuzzy Levenshtein distance is used to match what you say to the closest canonical object/command
- **Windows Speech Grammar Enrichment**: Automatically generated from CSV with 3,000+ command variants

This makes the system **very robust** even with noisy microphones and heavy accents. The fine-tuned model provides **90-95% accuracy** for astronomy commands.

### Available Commands

#### Navigation (GOTO)

| English | French | Action |
|---------|--------|--------|
| "Go to M31" | "Aller à M31" | Point to M31 |
| "Point to Jupiter" | "Pointer vers Jupiter" | Point to Jupiter |
| "Find Orion" | "Trouver Orion" | Point to Orion |
| "Show me Vega" | "Montre-moi Véga" | Point to Vega |

#### Telescope Control

| English | French | Action |
|---------|--------|--------|
| "Park telescope" | "Garer le télescope" | Park |
| "Start tracking" | "Démarrer le suivi" | Enable tracking |
| "Stop tracking" | "Arrêter le suivi" | Disable tracking |
| "Connect" | "Connecter" | ASCOM connection |

### Pronunciation Error Tolerance

The system accepts approximate pronunciations:

| What you say | What is understood |
|--------------|-------------------|
| "Goat to em thirty one" | goto M31 |
| "Beetlejuice" | Betelgeuse |
| "M forty-two" | M42 |

### Voice Feedback and Stats

For each **voice command actually executed**, the system provides:

- **Audio feedback** via text-to-speech, for example:
  - "Going to M31."
  - "Tracking started."
  - "M31 is below the horizon. GOTO blocked."
  - "Mount limits exceeded, command blocked."
- **On-screen stats** in the `Voice Control` panel:
  - Total commands received
  - Successful actions
  - Blocked/invalid commands (e.g. no connection, object below horizon, mount limits exceeded)
  - Errors (exceptions or ASCOM failures)

This allows you to evaluate the real performance of the voice system during an observing session.

---

## 📚 OBJECT CATALOGS

### ☀️ Planets (Solar System)

9 objects with real-time calculated positions:
Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune

### 🌌 Messier (M1-M110)

110 objects with fixed coordinates:
- **Nebulae**: M1 (Crab), M42 (Orion), M57 (Ring)...
- **Globular clusters**: M13 (Hercules), M22...
- **Open clusters**: M45 (Pleiades), M44 (Beehive)...
- **Galaxies**: M31 (Andromeda), M51 (Whirlpool)...

### ⭐ Bright Stars

40+ stars with magnitude and constellation:
Sirius, Vega, Arcturus, Betelgeuse, etc.

### 🌠 NGC/IC

Deep sky objects with search functionality. The NGC/IC catalog contains **dozens of popular targets**, including:

- North America Nebula (`NGC7000`), Fireworks Galaxy (`NGC6946`), California Nebula (`NGC1499`)
- Helix Nebula (`NGC7293`), Cat’s Eye Nebula (`NGC6543`), Double Cluster (`NGC869/NGC884`)
- Many well-known galaxies and clusters (e.g. `NGC2403`, `NGC2683`, `NGC2903`, `NGC4214`, `NGC7331`, etc.)

All these objects are also included in the **phonetic variants** for voice recognition.

### 📝 Custom Objects

Add your own objects with name, RA and Dec.

---

## 🎯 ADVANCED TRACKING

Advanced tracking combines multiple technologies for precise tracking.

### Workflow

1. **Connect camera** (optional)
2. **Start tracking**: The system captures images periodically
3. **Plate Solving**: Each image is analyzed to determine exact position
4. **Error calculation**: Difference between expected and actual position
5. **Kalman Filter**: Smooths measurements and predicts corrections
6. **Correction**: Automatic mount adjustment

---

## 🔍 PLATE SOLVING

Plate solving determines the exact telescope position by analyzing stars.

### Available Engines

| Engine | Type | Advantages | Disadvantages |
|--------|------|------------|---------------|
| **ASTAP** | Local | Fast (2-10s), offline | Requires installation |
| **Astrometry.net** | Online | No installation | Slower (30-120s), requires internet |

### ASTAP Configuration

1. Download ASTAP from www.hnsky.org/astap
2. Install in default folder
3. Download star catalogs (H17, H18, or G17)
4. The application automatically detects ASTAP

### Astrometry.net Configuration

1. Create an account on nova.astrometry.net
2. Get your API key from settings
3. Enter the key in **⚙️ API Credentials**

---

## 📐 KALMAN FILTER

The Kalman filter is a mathematical algorithm that improves tracking precision.

The Kalman filter:
- **Predicts** the future telescope position
- **Corrects** noisy plate solving measurements
- **Smooths** corrections to avoid jerky movements
- **Adapts** to your mount's behavior

---

## 🤖 MACHINE LEARNING (ML)

ML improves the Kalman filter by learning your mount's behavior.

### How it works

1. **Data collection**: The system records tracking errors
2. **Training**: An ML model learns error patterns
3. **Prediction**: The model predicts future errors
4. **Correction**: Predictions improve the Kalman filter

---

## 🌤️ WEATHER INTEGRATION

Weather data improves precision (atmospheric refraction) and ML.

Data displayed: Temperature, Humidity, Wind Speed, Cloud Cover, Visibility.

### Observer Profiles

The **Weather** tab allows you to define and save different **observer profiles**:

- Example profiles:
  - `Home` (your backyard)
  - `Observatory` (fixed location)
- Each profile stores:
  - Latitude / Longitude
  - Time zone
  - Mount type (for future advanced features)

You can switch from one site to another in one click; all horizon and mount-limit checks use the **current profile**.

---

## 💾 SESSION MANAGEMENT

### Features

| Feature | Description |
|---------|-------------|
| **📊 Statistics** | Objects observed, total time, errors |
| **📝 Notes** | Add notes to each observation |
| **💾 Save** | Export sessions to JSON |
| **📂 Load** | Resume a previous session |

---

## 🔧 TROUBLESHOOTING

### Telescope won't connect

1. Verify the ASCOM Alpaca server is running
2. Check the IP address and port

### Voice commands don't work

1. Verify microphone is authorized
2. Test with **🎙️ Test Mic**
3. For OpenAI: check your API key

### Plate solving fails

1. Verify ASTAP is installed (for local mode)
2. Check your internet connection (for Astrometry.net)

---

## 📄 LICENSE AND CREDITS

**HYBRID Telescope Control** v7.3 - Local AI Edition
© 2025 - All rights reserved

### Technologies used

- .NET Framework 4.8
- WPF (Windows Presentation Foundation)
- ASCOM Platform
- **Whisper.cpp** (Local speech-to-text)
- **Ollama + Mistral 3** (Local AI)
- OpenAI Whisper & GPT-4o-mini (Optional cloud)
- ML.NET
- OxyPlot
- NAudio

### New in v7.3

- ✅ **100% Local AI**: Whisper Local + Ollama for offline voice recognition
- ✅ **Fine-tuned Models**: 200k+ examples, 20k audio files
- ✅ **Auto-start**: Ollama starts automatically with CUDA/CPU detection
- ✅ **Home Position**: Telescope automatically goes to home on connection
- ✅ **Enhanced Safety**: Improved horizon verification
- ✅ **Unified Catalog**: All catalogs in one window with global search
- ✅ **Grammar Enrichment**: 3,000+ Windows Speech variants auto-generated

---

Last updated: December 2025
