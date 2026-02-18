from faster_whisper import WhisperModel

model = WhisperModel("tiny", device = "cpu", compute_type = "int8")

def transcribe(audio_path):
    segments, _ = model.transcribe(audio_path, beam_size = 1, vad_filter = True)
    
    trancript = ""

    for segment in segments:
        trancript += segment.text + " "

    return trancript
    