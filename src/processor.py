import openai
import os
from dotenv import load_dotenv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def process_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def summarize_peptide_article(text):
    prompt = f"Provide a concise summary of this peptide research article:\n\n{text}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
# scraped_content = "Text content of the scraped article"
# processed_text = process_text(scraped_content)
# summary = summarize_peptide_article(processed_text)

