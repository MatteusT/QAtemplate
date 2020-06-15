import os

from django.apps import AppConfig


MODEL = "distilbert-base-uncased-distilled-squad"
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DOCUMENT_NAME = ""

def extract_paragraphs():
    Document_path = os.path.join(DATA_PATH, DOCUMENT_NAME)
    return # paragraphs

def get_vectorizer_function(paragaphs):

    return # vectorizer_function



class QaGuiConfig(AppConfig):
    '''
    Initate the classes here
    '''
    name = 'qa_gui'
    paragraphs = extract_paragraphs()
    vectorizer = get_vectorizer_function(paragraphs)
    # transformer function(s)


