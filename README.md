# 🎬 AI Video Summarizer

An end-to-end local AI system that converts long videos into clean, structured summaries.

The application accepts **YouTube URLs or uploaded video files**, extracts speech, understands the content using a local LLM, and generates a human-readable summary.

This project demonstrates real AI engineering concepts: data ingestion → preprocessing → speech recognition → long-context reasoning → UI delivery.

---

## ✨ Features

* 🎥 Upload video files (mp4, mkv, mov, avi)
* 🔗 Paste YouTube URL
* 🔊 Direct audio extraction (no full video download required)
* 🧠 Speech-to-Text using Faster-Whisper
* 🧹 Transcript cleaning & noise removal
* 📚 Adaptive chunking for long videos
* 🤖 Local LLM summarization (Qwen GGUF via llama.cpp)
* 🖥️ Streamlit interactive UI
* 💻 Fully offline AI inference (no paid APIs)

---

## 🧠 System Architecture

User Input → Audio Extraction → Transcription → Cleaning → Chunking → LLM Reasoning → Structured Summary

```
User (Upload / URL)
        ↓
yt-dlp / File Handler
        ↓
FFmpeg Audio Processing
        ↓
Whisper Transcription
        ↓
Transcript Cleaning
        ↓
Chunking (long context handling)
        ↓
Qwen Local LLM
        ↓
Structured Summary Output
        ↓
Streamlit UI
```

---

## 🗂️ Project Structure

```
video_summarization/
│   app.py                 # Streamlit UI
│   main.py                # Pipeline orchestrator
│   requirements.txt
│
└── src/
    audio_transcriber.py   # Whisper STT
    extract_audio.py       # FFmpeg processing
    input_handler.py       # URL & upload handler
    text_cleaner.py        # Noise removal
    chunker.py             # Long text splitter
    text_summarizer.py     # Qwen summarization
```

---

## ⚙️ Installation

### 1. Clone repository

```
git clone https://github.com/<your-username>/video_summarization.git
cd video_summarization
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔧 Install FFmpeg (Required)

Download:
https://www.gyan.dev/ffmpeg/builds/

Add `ffmpeg/bin` to system PATH

Verify:

```
ffmpeg -version
```

---

## 🤖 Download LLM Model

The project uses a local quantized model:

**Qwen2.5-1.5B-Instruct-GGUF**

The model automatically downloads on first run and is cached locally.

---

## ▶️ Run Application

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 Example Output

The system generates:

* Video type detection
* Main topic
* Key points
* Important details
* Final clean summary

---

## 🧩 Technologies Used

| Component          | Technology               |
| ------------------ | ------------------------ |
| Speech Recognition | Faster-Whisper           |
| LLM                | Qwen2.5 GGUF (llama.cpp) |
| Video Processing   | FFmpeg                   |
| YouTube Download   | yt-dlp                   |
| Backend Logic      | Python                   |
| UI                 | Streamlit                |

---

## 🚀 Future Improvements

* Timestamped chapter generation
* Highlight extraction (key moments)
* Subtitle (.srt) generation
* Multilingual summarization
* FastAPI model server deployment
* Vector database search inside videos

---

## 👨‍💻 Author

**Shivam Gehlot**

Aspiring AI Engineer focused on building practical ML systems and local-AI applications.

---

## 📜 License

MIT License
