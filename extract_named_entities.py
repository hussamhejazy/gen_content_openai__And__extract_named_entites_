import spacy

def extract(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text) 
    return doc.ents


#pip install spacy

#python -m spacy download en_core_web_sm