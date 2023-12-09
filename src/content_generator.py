import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_peptide_content(summary, platform='blog'):
    if platform == 'twitter':
        tweet_prompt = f"Create an engaging tweet about this peptide research finding:\n\n{summary}"
        max_length = 280
    else:
        article_prompt = f"Write an informative short article about these peptide research findings:\n\n{summary}"
        max_length = 500

    response = openai.Completion.create(
        engine="davinci",
        prompt=(tweet_prompt if platform == 'twitter' else article_prompt),
        max_tokens=max_length
    )
    return response.choices[0].text.strip()

# Example usage
# summary = "Summary of the peptide article"
# content_for_twitter = generate_peptide_content(summary, 'twitter')
# content_for_blog = generate_peptide_content(summary, 'blog')

