import time
from transformers import pipeline
from utils import split_into_chunks

def load_summarizer():
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        revision="main",
        device_map="auto"
    )
    return summarizer

def summarize_text(text: str, summarizer_fn, max_time: int = 15) -> str:
    chunks = split_into_chunks(text)
    summaries = []
    start = time.time()

    for chunk in chunks:
        if time.time() - start > max_time:
            summaries.append("⏱️ Stopped early due to time limit.")
            break
        summary = summarizer_fn(chunk)[0]["summary_text"]
        summaries.append(summary)

    return "\n\n".join(summaries)
