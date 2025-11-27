import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Set up the Streamlit interface
st.title("Web Scraper Agent")
st.write("This agent scrapes a website and uses Gemini to analyze the content.")

# Get user input for the URL and API key
url = st.text_input("Enter the URL of the website you want to scrape:")
api_key = st.text_input("Enter your Gemini API Key:", type="password")

# Add a button to trigger the scraping
if st.button("Scrape and Analyze"):
    if url and api_key:
        try:
            # Configure the Gemini API
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            # Scrape the website
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            scraped_text = soup.get_text()

            # Use Gemini to analyze the scraped text
            prompt = f"Summarize the following text from the website {url}:\n\n{scraped_text}"
            generation = model.generate_content(prompt)

            # Display the results
            st.subheader("Scraped Text Summary")
            st.write(generation.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both a URL and your Gemini API Key.")
