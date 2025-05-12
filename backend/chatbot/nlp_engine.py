# NLP Engine code (Chat with GPT-4 & Hindi/English Detection)
import openai
import os
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_language(text):
    try:
        language = detect(text)
        if language == 'hi':
            return 'hi'
        elif language == 'en':
            return 'en'
        else:
            return 'unknown'
    except LangDetectException:
        return 'unknown'

def generate_reply(prompt, language='en'):
    system_prompt = "You are a compassionate mental health assistant. Reply in a friendly, warm, and caring tone."

    if language == 'hi':
        system_prompt += " You must reply in Hindi."
    else:
        system_prompt += " You must reply in English."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Sorry, I am unable to respond right now. ({str(e)})"

def detect_language_and_generate_reply(text):
    lang = detect_language(text)
    return generate_reply(text, language=lang)

