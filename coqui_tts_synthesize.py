#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script wrapper pour Coqui TTS - Appelé depuis C#
Synthétise du texte en audio et retourne le fichier audio en base64
"""
import sys
import os
import json
import base64
import tempfile
import traceback

# Ajouter le chemin du dossier coqui tts au PYTHONPATH
coqui_tts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BOGDAN WHISPER TRAINED", "coqui tts")
if os.path.exists(coqui_tts_dir):
    sys.path.insert(0, coqui_tts_dir)

try:
    from coqui_tts import CoquiTTS
except ImportError:
    # Essayer d'importer depuis le Python portable
    python_portable = os.path.join(coqui_tts_dir, "python", "python.exe")
    if os.path.exists(python_portable):
        # Si on est appelé depuis C#, on ne peut pas changer l'interpréteur
        # Mais on peut essayer d'ajouter le chemin Python portable
        python_lib = os.path.join(coqui_tts_dir, "python", "Lib", "site-packages")
        if os.path.exists(python_lib):
            sys.path.insert(0, python_lib)
        try:
            from coqui_tts import CoquiTTS
        except ImportError:
            print(json.dumps({"error": "Coqui TTS module not found. Please ensure coqui_tts.py is in the coqui tts directory."}))
            sys.exit(1)
    else:
        print(json.dumps({"error": "Coqui TTS module not found. Please ensure coqui_tts.py is in the coqui tts directory."}))
        sys.exit(1)

def synthesize_text(text, language="en", speaker_wav=None, model_name=None):
    """
    Synthétise du texte en audio
    
    Args:
        text: Texte à synthétiser
        language: Langue (en, fr, es, etc.)
        speaker_wav: Chemin vers fichier audio de référence (optionnel)
        model_name: Nom du modèle (optionnel, utilise le défaut si None)
    
    Returns:
        Dict avec 'success', 'audio_base64', 'sample_rate', 'error'
    """
    try:
        # Initialiser Coqui TTS
        if model_name:
            tts = CoquiTTS(model_name=model_name)
        else:
            # Utiliser XTTS v2 par défaut (meilleure qualité, multilingue)
            # Note: XTTS v2 nécessite speaker_wav pour le clonage de voix
            tts = CoquiTTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
        
        if not tts.initialize():
            return {
                "success": False,
                "error": "Failed to initialize Coqui TTS"
            }
        
        # Vérifier si le modèle nécessite speaker_wav
        requires_speaker = tts._is_voice_cloning_model()
        
        if requires_speaker and not speaker_wav:
            # Essayer de trouver un fichier audio par défaut
            # Chercher dans plusieurs emplacements possibles
            # Chercher un fichier audio de référence dans plusieurs emplacements possibles
            # Note: XTTS v2 nécessite un fichier audio de 3-10 secondes avec une voix claire
            possible_speakers = [
                os.path.join(coqui_tts_dir, "default_speaker.wav"),
                os.path.join(coqui_tts_dir, "speaker.wav"),
                os.path.join(coqui_tts_dir, "reference.wav"),
                os.path.join(coqui_tts_dir, "Enregistrement.mp3"),  # D'après generer_audio.py
                os.path.join(coqui_tts_dir, "Enregistrement.wav"),
                # Chercher aussi dans le répertoire parent (au cas où)
                os.path.join(os.path.dirname(coqui_tts_dir), "Enregistrement.mp3"),
                os.path.join(os.path.dirname(coqui_tts_dir), "Enregistrement.wav"),
            ]
            
            speaker_wav = None
            for speaker_path in possible_speakers:
                if os.path.exists(speaker_path):
                    # Si c'est un MP3, on peut l'utiliser directement (Coqui TTS supporte MP3)
                    # Sinon, utiliser le fichier tel quel
                    speaker_wav = speaker_path
                    break
            
            if not speaker_wav:
                # Créer un message d'erreur informatif
                return {
                    "success": False,
                    "error": f"Model {tts.model_name} requires a speaker_wav file for voice cloning. Please provide one in the coqui tts directory (default_speaker.wav, speaker.wav, or Enregistrement.mp3)."
                }
        
        # Synthétiser
        result = tts.synthesize(text, language=language, speaker_wav=speaker_wav)
        
        if result is None:
            return {
                "success": False,
                "error": "Synthesis failed"
            }
        
        sample_rate, audio_array = result
        
        # Sauvegarder dans un fichier temporaire
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            output_path = tmp_file.name
        
        # Utiliser torchaudio pour sauvegarder (si disponible)
        try:
            import torchaudio
            import torch
            # Convertir numpy array en tensor
            audio_tensor = torch.from_numpy(audio_array).unsqueeze(0) if len(audio_array.shape) == 1 else torch.from_numpy(audio_array)
            torchaudio.save(output_path, audio_tensor, sample_rate)
        except:
            # Fallback: utiliser scipy ou wave
            try:
                from scipy.io import wavfile
                wavfile.write(output_path, int(sample_rate), audio_array)
            except:
                import wave
                import numpy as np
                # Convertir en int16
                audio_int16 = (audio_array * 32767).astype(np.int16)
                with wave.open(output_path, 'wb') as wav_file:
                    wav_file.setnchannels(1)  # Mono
                    wav_file.setsampwidth(2)  # 16-bit
                    wav_file.setframerate(int(sample_rate))
                    wav_file.writeframes(audio_int16.tobytes())
        
        # Lire le fichier et convertir en base64
        with open(output_path, 'rb') as f:
            audio_bytes = f.read()
        
        # Nettoyer
        try:
            os.unlink(output_path)
        except:
            pass
        
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        
        return {
            "success": True,
            "audio_base64": audio_base64,
            "sample_rate": int(sample_rate)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }

if __name__ == "__main__":
    # Lire les arguments depuis stdin (JSON)
    try:
        input_data = json.loads(sys.stdin.read())
        text = input_data.get("text", "")
        language = input_data.get("language", "en")
        speaker_wav = input_data.get("speaker_wav", None)
        model_name = input_data.get("model_name", None)
        
        if not text:
            print(json.dumps({"success": False, "error": "No text provided"}))
            sys.exit(1)
        
        result = synthesize_text(text, language, speaker_wav, model_name)
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }))
        sys.exit(1)
