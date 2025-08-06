import streamlit as st
import requests
from nltk.tokenize import sent_tokenize

# Replace this with your own NewsAPI key
API_KEY = '591f6f8d6ddc4283b5c85f1500907aa8'

def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=591f6f8d6ddc4283b5c85f1500907aa8'
    response = requests.get(url)

    # Debug output to Streamlit
    st.write("Status Code:", response.status_code)

    try:
        data = response.json()
        st.write("API Response:", data)  # This will print the whole JSON so we can debug
        return data.get('articles', [])
    except Exception as e:
        st.error(f"Error parsing response: {e}")
        return []


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
        if article.get('url'):
            st.markdown(f"[Read full article]({article['url']})")
