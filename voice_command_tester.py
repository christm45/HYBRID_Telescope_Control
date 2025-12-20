#!/usr/bin/env python3
"""
Voice Command Tester - Records audio from microphone and transcribes using Whisper
Compatible with HYBRID Telescope Control System
"""

import sys
import json
import argparse
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import tempfile
import os

# Initialize model (will be loaded once)
model = None

def load_model():
    """Load Whisper medium model"""
    global model
    if model is None:
        print("[Whisper] Loading medium model...", file=sys.stderr, flush=True)
        try:
            model = WhisperModel("medium", device="cpu", compute_type="int8")
            print("[Whisper] Model loaded successfully", file=sys.stderr, flush=True)
        except Exception as e:
            print(f"[Whisper] Error loading model: {e}", file=sys.stderr, flush=True)
            raise
    return model

def record_audio(duration=5.0, sample_rate=16000):
    """Record audio from default microphone"""
    try:
        print(f"[Audio] Recording for {duration} seconds...", file=sys.stderr, flush=True)
        print("[Audio] Speak now...", file=sys.stderr, flush=True)
        
        # Record audio
        audio_data = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()  # Wait until recording is finished
        
        print("[Audio] Recording finished", file=sys.stderr, flush=True)
        
        # Check if audio is not silent
        max_amplitude = np.max(np.abs(audio_data))
        if max_amplitude < 0.01:  # Very quiet threshold
            return None, "No audio detected - microphone may be muted or not working"
        
        return audio_data.flatten(), None
    except Exception as e:
        return None, f"Recording error: {str(e)}"

def transcribe_audio(audio_data, sample_rate=16000, language_code="auto"):
    """Transcribe audio data using Whisper"""
    try:
        whisper_model = load_model()
        
        # Transcribe with faster-whisper
        segments, info = whisper_model.transcribe(
            audio_data,
            sample_rate=sample_rate,
            language=language_code if language_code != "auto" else None,
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500)
        )
        
        # Get full transcription
        full_text = ""
        confidence_sum = 0.0
        segment_count = 0
        
        for segment in segments:
            full_text += segment.text + " "
            confidence_sum += segment.avg_logprob
            segment_count += 1
        
        full_text = full_text.strip()
        avg_confidence = confidence_sum / segment_count if segment_count > 0 else 0.0
        
        if not full_text:
            return {
                "success": False,
                "text": "",
                "error": "no_transcription",
                "message": "Could not transcribe audio - no speech detected"
            }
        
        return {
            "success": True,
            "text": full_text,
            "language": info.language,
            "confidence": float(avg_confidence),
            "message": "Transcription successful"
        }
    except Exception as e:
        import traceback
        error_msg = f"{str(e)}"
        return {
            "success": False,
            "text": "",
            "error": "transcription_error",
            "message": f"Transcription failed: {error_msg}"
        }

def main():
    parser = argparse.ArgumentParser(description="Voice Command Tester - Record and transcribe audio")
    parser.add_argument("--api-once", action="store_true", help="One-shot API mode (record once and return JSON)")
    parser.add_argument("--duration", type=float, default=5.0, help="Recording duration in seconds")
    parser.add_argument("--language", type=str, default="auto", help="Language code (e.g., en, fr) or 'auto'")
    parser.add_argument("--sample-rate", type=int, default=16000, help="Audio sample rate")
    
    args = parser.parse_args()
    
    # Check if sounddevice is available
    try:
        devices = sd.query_devices()
        default_input = sd.default.device[0]
        print(f"[Audio] Using input device: {devices[default_input]['name']}", file=sys.stderr, flush=True)
    except Exception as e:
        result = {
            "success": False,
            "text": "",
            "error": "audio_device_error",
            "message": f"Could not access audio devices: {str(e)}"
        }
        print(json.dumps(result, ensure_ascii=False))
        sys.exit(1)
    
    # Record audio
    audio_data, error = record_audio(args.duration, args.sample_rate)
    
    if error:
        result = {
            "success": False,
            "text": "",
            "error": "recording_error",
            "message": error
        }
        print(json.dumps(result, ensure_ascii=False))
        sys.exit(1)
    
    if audio_data is None:
        result = {
            "success": False,
            "text": "",
            "error": "no_audio",
            "message": "No audio recorded - check microphone"
        }
        print(json.dumps(result, ensure_ascii=False))
        sys.exit(1)
    
    # Transcribe
    result = transcribe_audio(audio_data, args.sample_rate, args.language)
    
    # Output JSON result
    print(json.dumps(result, ensure_ascii=False))
    
    # Exit with error code if transcription failed
    if not result["success"]:
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        result = {
            "success": False,
            "text": "",
            "error": "interrupted",
            "message": "Recording interrupted by user"
        }
        print(json.dumps(result, ensure_ascii=False))
        sys.exit(1)
    except Exception as e:
        import traceback
        result = {
            "success": False,
            "text": "",
            "error": "unexpected_error",
            "message": f"Unexpected error: {str(e)}\n{traceback.format_exc()}"
        }
        print(json.dumps(result, ensure_ascii=False))
        sys.exit(1)
