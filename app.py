import streamlit as st
from summarizer import summarize_text, load_summarizer
from extractor import extract_from_url, extract_from_pdf
from utils import MAX_TEXT_LENGTH
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(page_title="🧠 Universal Summarizer", layout="centered")
summarizer_fn = None

st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #fff;
        }
        h1 {
            color: white;
            text-align: center;
            font-size: 2.2rem;
            font-weight: bold;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #2c2c2c;
            color: white;
            padding: 0.75rem 1rem;
            border-radius: 6px 6px 0 0;
            font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #6366f1;
            color: white;
        }
        button[kind="primary"] {
            background-color: #6366f1 !important;
            color: white !important;
            border: none;
        }
        .stFileUploader, .stTextInput, .stTextArea {
            background-color: #1e1e1e !important;
            color: white !important;
        }
        .centered-box {
            max-width: 600px;
            margin: 0 auto;
            padding: 1rem;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: gray;
            font-size: 0.85rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>SimplyText AI</h1>", unsafe_allow_html=True)

tabs = st.tabs(["🔗 Add URL", "📋 Add text", "📎 Upload file"])
raw_text = ""

with tabs[0]:
    st.markdown('<div class="centered-box">', unsafe_allow_html=True)
    url = st.text_input("Paste blog/article URL")
    if st.button("Summarize This", key="url_summary"):
        with st.spinner("Extracting content from URL..."):
            text = extract_from_url(url)
            if text and len(text) > 100:
                raw_text = text[:MAX_TEXT_LENGTH]
            else:
                st.error("❌ Could not extract text or it is too short.")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="centered-box">', unsafe_allow_html=True)
    input_text = st.text_area("Paste your text below:", height=300)
    if st.button("Summarize This", key="text_summary"):
        if len(input_text.strip()) > 0:
            raw_text = input_text.strip()[:MAX_TEXT_LENGTH]
        else:
            st.error("❌ Please paste some text to summarize.")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="centered-box">', unsafe_allow_html=True)
    st.write("We support `.pdf` files up to 25 MB.")
    uploaded_file = st.file_uploader("Select or Drop a file", type=["pdf"])
    if uploaded_file and st.button("Summarize This", key="file_summary"):
        with st.spinner("Extracting PDF content..."):
            text = extract_from_pdf(uploaded_file)
            if text and len(text) > 100:
                raw_text = text[:MAX_TEXT_LENGTH]
            else:
                st.error("❌ Could not extract text from PDF.")
    st.markdown('</div>', unsafe_allow_html=True)

if raw_text:
    with st.spinner("Loading summarizer..."):
        if summarizer_fn is None:
            try:
                summarizer_fn = load_summarizer()
            except Exception as e:
                st.error(f"❌ Failed to load model: {str(e)}")
                st.stop()

    with st.spinner("Summarizing..."):
        try:
            summary = summarize_text(raw_text, summarizer_fn)
            st.subheader("📝 Summary")
            st.success(summary)
            st.download_button("⬇️ Download Summary", summary, file_name="summary.txt", mime="text/plain")
        except Exception as e:
            st.error(f"❌ Error generating summary: {str(e)}")

st.markdown('<footer>@CHINMOY DEB<br>© 2025</footer>', unsafe_allow_html=True)
