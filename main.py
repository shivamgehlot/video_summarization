from src.input_handler import download_audio_from_youtube, save_uploaded_video
from src.extract_audio import extract_speech
from src.audio_transcriber import transcribe
from src.text_cleaner import clean_transcript
from src.text_summarizer import summarize_transcript

def get_audio_source(url = None, uploaded_file = None):

    if url:
        return download_audio_from_youtube(url)
    
    if uploaded_file:
        video = save_uploaded_video(uploaded_file)
        return extract_speech(video)

    raise ValueError("No input provided")

def run_pipeline(url = None, uploaded_file = None):

    audio = get_audio_source(url, uploaded_file)

    transcript = transcribe(audio)
    transcript = clean_transcript(transcript)

    summary = summarize_transcript(transcript)

    return summary




