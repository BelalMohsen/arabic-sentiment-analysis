# Natural Language Toolkit: code_document_classify_fd
import nltk
from nltk.corpus import movie_reviews
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000] # [_document-classify-all-words]

def document_features(document): # [_document-classify-extractor]
    document_words = set(document) # [_document-classify-set]
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
features=document_features("very happy to see you again my friend")
print(features)
