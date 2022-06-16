import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# IBM Watson language translator instance

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#English to French
def englishToFrench(english_text):
    translation = language_translator.translate(
        text= english_text,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

#French to English
def frenchToEnglish(french_text):
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
