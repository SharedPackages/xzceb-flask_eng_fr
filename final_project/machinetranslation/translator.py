import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import ApiException

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return translation

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return translation