"""
Load required packages
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Function to translate English to French
def english_to_french(english_text):
    """
    English to French
    """
    translation = language_translator.translate(text=english_text,
     model_id = "en-fr").get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

# Function to translate French to English
def french_to_english(french_texts):
    """
    Input language translate function
    """
    transalation = language_translator.translate(text=french_texts,
     model_id = "en-fr").get_result()
    english_texts = transalation['translations'][0]['translation']
    return english_texts
