import spacy
import json
from fetch import scraper

def get_article_text(url):
    raw_json = scraper(url)
    parsed = json.loads(raw_json)
    return parsed["raw_text"]

def get_claims(url, top_n=8):
    
    nlp = spacy.load("en_core_web_sm")
    text = get_article_text(url)
    doc = nlp(text)
    sents = list(doc.sents)

    scored = []

    for s in sents:
        if s.text.strip().endswith("?"):
            continue
        if s[0].pos_ == "VERB":
            continue

        entity_count = len(s.ents)
        if entity_count > 0:
            scored.append((entity_count, s.text))

    scored.sort(key=lambda pair: pair[0], reverse=True)

    top_claims = [text for count, text in scored[:top_n]]
    return top_claims