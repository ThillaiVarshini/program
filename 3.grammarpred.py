import spacy
import pandas as pd
nlp = spacy.load("en_core_web_sm")
def extract(sentence):
    doc = nlp(sentence)
    noun = []
    verb = []
    adjective = []
    adverb=[]
    for token in doc:
        if token.pos_ == "NOUN":
            noun.append(token)
        elif token.pos_ == "VERB":
            verb.append(token)
        elif token.pos_ == "ADJ":
            adjective.append(token)
        elif token.pos_ == "ADV":
            adverb.append(token)    
    return noun, verb, adjective,adverb
sentence_df = pd.read_csv('textclassification.csv')
all_nouns = []
all_verbs = []
all_adjectives = []
all_adverb = []
for sentence in sentence_df['sentence']:
    noun, verb, adjective,adverb = extract(sentence)
    all_nouns.extend(noun)
    all_verbs.extend(verb)
    all_adjectives.extend(adjective)
    all_adverb.extend(adverb)
print("\n\n All Verbs  :\n\n ", all_verbs)
print("\n\n All Nouns  : \n\n", all_nouns)
print("\n\n All Adjectives  : ", all_adjectives)
print("\n\n All Adverbs : ", all_adverb)

