from moviepy import VideoFileClip

def extract_speech(video_file):
    # Extract Audio
    video = VideoFileClip(video_file)   
    audio_path = "temp/audio.wav"
    video.audio.write_audiofile(
        audio_path,
        fps = 16000,
        nbytes = 2,
        codec = "pcm_s16le",
        ffmpeg_params=["-ac", "1"]  # mono
    )

    return audio_path
    