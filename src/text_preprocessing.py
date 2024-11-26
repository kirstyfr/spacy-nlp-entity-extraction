import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def data_preprocess(text):
    text  = text.lower()
    text = re.sub('\W+',' ', text)    
    return text

def tokenize_text(text):
    text = word_tokenize(text)    
    text = [word for word in text if word not in stop_words]    
    return text