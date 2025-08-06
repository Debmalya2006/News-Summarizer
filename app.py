Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import streamlit as st
import requests
from nltk.tokenize import sent_tokenize

# Replace this with your own NewsAPI key
API_KEY = '591f6f8d6ddc4283b5c85f1500907aa8'

def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={591f6f8d6ddc4283b5c85f1500907aa8}'
    response = requests.get(url)
    data = response.json()
    return data['articles']

def summarize_text(text, max_sentences=2):
    sentences = sent_tokenize(text)
    return ' '.join(sentences[:max_sentences])

# Streamlit App
st.title("📰 News Summarizer")
st.write("Get top Indian news headlines with short summaries.")

if st.button("Fetch News"):
    articles = fetch_news()
    for article in articles[:5]:
        st.subheader(article['title'])
        if article['description']:
            summary = summarize_text(article['description'])
            st.write(summary)
        if article['url']:
            st.markdown(f"[Read full article]({article['url']})")
