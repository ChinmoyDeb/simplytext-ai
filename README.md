# 🧠 SimplyText AI — A Universal Text Summarizer

**SimplyText AI** is a GenAI-powered Streamlit app that summarizes blogs, articles, PDFs, or custom text using HuggingFace's `facebook/bart-large-cnn` model. It provides a minimal, dark-themed UI with 3 summarization options: Paste Text, URL, or File Upload.

---

## 🚀 Features

- 🔗 Summarize content from any public URL
- 📋 Paste and summarize any raw text
- 📎 Upload `.pdf` files and get a summary
- 🤖 Uses HuggingFace Transformers (`facebook/bart-large-cnn`)
- 🖤 Modern dark-themed UI built with Streamlit

---

## 🧰 Tech Stack

- Python 3.10+
- Streamlit
- Transformers (Hugging Face)
- Torch
- pdfplumber
- BeautifulSoup
- Requests

---

## 🔧 Installation

```bash
# 1. Clone the repository
git clone https://github.com/ChinmoyDEB/simplytext-ai.git
cd simplytext-ai

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
