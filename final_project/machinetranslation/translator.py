"""
Module for translating text between English and French.
"""

import os
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    Translates English text to French.

    :param english_text: The English text to translate.
    :return: The translated French text.
    """
    translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.

    :param french_text: The French text to translate.
    :return: The translated English text.
    """
    translation2 = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = json.dumps(translation2, indent=2, ensure_ascii=False)
    return english_text
