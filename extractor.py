import requests
from bs4 import BeautifulSoup
import pdfplumber

def extract_from_url(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.find_all(["p", "article"])
        return " ".join(p.get_text() for p in paragraphs).strip()
    except Exception:
        return None

def extract_from_pdf(file) -> str:
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text.strip()
    except:
        return None
