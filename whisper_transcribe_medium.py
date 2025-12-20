#!/usr/bin/env python3
"""
Whisper Medium Transcription Service
Transcribes audio using faster-whisper medium model
"""

import sys
import json
import argparse
import base64
import io
import wave
import numpy as np
from faster_whisper import WhisperModel

# Initialize model (will be loaded once)
model = None

def load_model():
    """Load Whisper medium model"""
    global model
    if model is None:
        print("[Whisper] Loading medium model...", file=sys.stderr, flush=True)
        model = WhisperModel("medium", device="cpu", compute_type="int8")
        print("[Whisper] Model loaded", file=sys.stderr, flush=True)
    return model

def transcribe_audio(audio_data, language_code="auto"):
    """Transcribe audio data"""
    try:
        whisper_model = load_model()
        
        # Decode base64 audio
        audio_bytes = base64.b64decode(audio_data)
        
        # Convert raw PCM to numpy array for faster-whisper
        import numpy as np
        
        # faster-whisper expects numpy array of float32 in range [-1.0, 1.0]
        # Input is 16-bit PCM (2 bytes per sample), little-endian
        audio_array = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0
        sample_rate = 16000  # Fixed sample rate from WaveInEvent
        
        # Transcribe with faster-whisper
        segments, info = whisper_model.transcribe(
            audio_array,
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
        
        return {
            "transcription": full_text,
            "language": info.language,
            "confidence": avg_confidence,
            "success": True
        }
    except Exception as e:
        import traceback
        error_msg = f"{str(e)}\n{traceback.format_exc()}"
        return {
            "transcription": "",
            "error": error_msg,
            "success": False
        }

def main():
    parser = argparse.ArgumentParser(description="Whisper Medium Transcription Service")
    parser.add_argument("--audio", type=str, required=True, help="Base64 encoded audio data")
    parser.add_argument("--language", type=str, default="auto", help="Language code (e.g., en, fr) or 'auto'")
    parser.add_argument("--format", type=str, default="json", help="Output format: json or text")
    
    args = parser.parse_args()
    
    result = transcribe_audio(args.audio, args.language)
    
    if args.format == "text":
        if result["success"]:
            print(result["transcription"])
        else:
            print(f"ERROR: {result.get('error', 'Unknown error')}", file=sys.stderr)
            sys.exit(1)
    else:
        print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
