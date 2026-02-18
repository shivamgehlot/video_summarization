from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from src.chunker import chunk_text

model_path = hf_hub_download(
	repo_id="Qwen/Qwen2.5-1.5B-Instruct-GGUF",
	filename="qwen2.5-1.5b-instruct-q4_k_m.gguf",
)

llm = Llama(
    model_path = model_path,
    n_ctx = 4096,
    n_threads = 8,
    n_batch = 512,
    verbose = False
)

def summarize_chunk(text):

    prompt = f"""
You are an intelligent video understanding system.

STEP 1 — Identify the video type from the transcript:
Possible types:
- lecture / educational
- tutorial / how-to
- interview / podcast
- vlog / lifestyle
- story / entertainment
- news / informational
- discussion / debate

STEP 2 — Extract the important information depending on type:

Rules:
- Remove filler words and repeated dialogue
- Focus on meaning, not exact sentences
- Merge similar ideas
- Ignore greetings, jokes, and small talk

STEP 3 — Produce structured output in this format:

VIDEO TYPE:
<detected type>

MAIN TOPIC:
<one sentence>

KEY POINTS:
- bullet points explaining the important content

IMPORTANT DETAILS:
- names / concepts / steps / facts mentioned

FINAL SUMMARY:
Write a clean human-readable paragraph explaining the video.

Transcript:
{text}

Summary:
"""

    output = llm(
        prompt,
        max_tokens=400,
        temperature=0.2,
        stop=["</s>"]
    )

    return output["choices"][0]["text"].strip()

def summarize_transcript(transcript):

    chunks = chunk_text(transcript)

    partial_summaries = []

    for chunk in chunks:
        summary = summarize_chunk(chunk)
        partial_summaries.append(summary)
    
    combined = "\n".join(partial_summaries)

    final = summarize_chunk(combined)

    return final