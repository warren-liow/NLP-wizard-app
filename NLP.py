import sys
import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
import numpy as np
from datascience import *
import warnings
warnings.simplefilter('ignore', FutureWarning)
from nltk.text import Text
import spacy
from nltk.corpus import wordnet as wn
from gensim import corpora, models
#from contractions import CONTRACTION_MAP
import string
punctuation_list = string.punctuation

# arguments
text= sys.argv[1]
function= sys.argv[2]
word=sys.argv[3]

# function
def process(text, function, word):
    research_text=Text(word_tokenize(text))
    def remove_punctuation(my_tokenized_text):
        return [word for word in my_tokenized_text if word not in punctuation_list]
    def remove_dashes(my_tokenized_text):
        return [word for word in my_tokenized_text if word != "--"]
    tokens_nopunct = remove_dashes(remove_punctuation(research_text))
    
    if function=="count":
        print(research_text.count(word))
    elif function=="similar":
        research_text.similar(word)
    elif function=="lexical diversity":
        print("The lexical diversity of the text (most punctuation removed) is: " + str(len(set(tokens_nopunct))/len(tokens_nopunct)))
    elif function=="most common words":
        print(FreqDist(tokens_nopunct).most_common(50))

process(text, function, word)
