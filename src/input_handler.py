import os
import yt_dlp
import shutil

TEMP_DIR = "temp"

def ensure_temp():
    os.makedirs(TEMP_DIR, exist_ok=True)

# youtube upload
def download_audio_from_youtube(url):

    ensure_temp()

    output = os.path.join(TEMP_DIR, "yt_audio.%(ext)s")

    ydl_opts = {
        "format" : "bestaudio/best",
        "outtmpl" : output,
        "quiet" : True,
        "noplaylist" : True,
        "postprocessors" : [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192"
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return os.path.join(TEMP_DIR, "yt_audio.wav")

# Manual upload

def save_uploaded_video(uploaded_file):
    ensure_temp()

    path = os.path.join(TEMP_DIR, uploaded_file.name)

    with open(path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    return path
