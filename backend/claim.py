import spacy
import json
from fetch import scraper

def get_article_text():
    raw_json = scraper()
    parsed = json.loads(raw_json)
    return parsed["raw_text"]

def get_claim():
    
    nlp = spacy.load("en_core_web_sm")

    text = get_article_text()

    doc = nlp(text)