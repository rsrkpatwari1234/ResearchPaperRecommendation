import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
import numpy as np
import sys
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from num2words import num2words
from spellchecker import SpellChecker

stopwords = set(stopwords.words('english'))


class PreProcessing:
    def __init__(self):
        pass

    def convert_to_lowercase(self,sentence):
        #converting string to lower case
        return sentence.lower()

    def extract_tokens(self,sentence):
        #extracting tokens from the text 
        tokens = word_tokenize(sentence)
        tokens = [token for token in tokens if token.isalpha() or token.isnumeric()]
        return tokens 

    def checkspell(self,tokens):
        #checking spelling of each token
        spell = SpellChecker()
        spell.distance = 1  # for lengthy words
        corrected_word_tokens=[]
        for token in tokens:
          corrected_word_tokens.append(spell.correction(token))

        return corrected_word_tokens

    def convert_num_to_words(self,tokens):
        new_sentence = []
        for i in tokens:
          if i.isnumeric(): 
            new_sentence.append(num2words(i))
          else:
            new_sentence.append(i);
        return new_sentence

    def remove_stopwords(self,tokens):
        tokens = [token for token in tokens if token not in stopwords]
        return tokens

    def lemmatized_tokens(self, tokens):
        #pass the wordnet_tagged tokens
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized_tokens

    def add_synonyms(self,tokens):
        synonyms=[]
        for token in tokens:
          for syn in wordnet.synsets(token): 
            for l in syn.lemmas(): 
                synonyms.append(l.name()) 

        return synonyms

def parse_query(querystr):
    pp = PreProcessing()
    lowercase_sentence = pp.convert_to_lowercase(querystr)
    tokens = pp.extract_tokens(lowercase_sentence)
    corrected_tokens = pp.checkspell(tokens)
    tokens_words = pp.convert_num_to_words(corrected_tokens)
    tokens_without_stopwords = pp.remove_stopwords(tokens_words)
    lemmat_tokens = pp.lemmatized_tokens(tokens_without_stopwords)
    final_query = pp.add_synonyms(lemmat_tokens)

    return final_query
    
if __name__ == '__main__':
    querystr = "transport; in. seniconductors"
    final_query = parse_query(querystr)
    print(final_query);
    