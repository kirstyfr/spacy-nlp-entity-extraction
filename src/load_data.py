import csv 
import sys
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import os



def load_abstracts_clean_data_name(abstract_file_name, extractor, max_rows=500, batch_size=2, clean_data=False):
    abstract_list = []
    abstract_ids = []
    row_count = 0
    
    # Construct file path using the provided file_name
    file_path = os.path.join('/root/DS_Evidence/ds_project_folder/data/raw_data/CHEMNER/', abstract_file_name + '.txt')
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        
        while row_count < max_rows:
            batch = []
            try:
                for _ in range(batch_size):
                    row = next(reader)
                    batch.append(row)
            except StopIteration:
                break

            for row in batch:
                if row_count >= max_rows:
                    break
            
                entities = extractor.extract_entities(row[2],tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased"))
                
                if clean_data:
                    entities = [(data_preprocess(entity[0]), *entity[1:]) if isinstance(entity, tuple) else data_preprocess(entity) for entity in entities]
                
                abstract_list.append([row[0], entities])
                abstract_ids.append(row[0])
                row_count += 1

            sys.stdout.write("\rRows processed: {}".format(row_count))
            sys.stdout.flush()
            
    return abstract_list, abstract_ids, abstract_file_name



def load_abstracts_clean_BERT(file_path, extractor, max_rows=500, batch_size=2, clean_data=False):
    abstract_list = []
    abstract_ids = []
    row_count = 0
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        
        while row_count < max_rows:
            batch = []
            try:
                for _ in range(batch_size):
                    row = next(reader)
                    batch.append(row)
            except StopIteration:
                break

            for row in batch:
                if row_count >= max_rows:
                    break
                try:
                    entities = extractor.extract_entities(row[2])
                    if clean_data:
                        entities = [(data_preprocess(entity[0]), *entity[1:]) if isinstance(entity, tuple) else data_preprocess(entity) for entity in entities]
                    abstract_list.append([row[0], entities])
                    abstract_ids.append(row[0])
                    row_count += 1
                    sys.stdout.write("\rRows processed: {}".format(row_count))
                    sys.stdout.flush()
                except RuntimeError as e:
                    # Print the article ID when the error occurs
                    print("\nError processing Article ID:", row[0])
                    print("Error:", e)
                    continue
            
    return abstract_list, abstract_ids


def load_annotations(file_path, abstract_ids, clean_data=False): 
    annotation_list = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            annotation_text = data_preprocess(row[4]) if clean_data else row[4]
            reordered_list = (annotation_text, int(row[2]), int(row[3]))
            if row[0] in abstract_ids:
                annotation_list.append([row[0], reordered_list])                          
    return annotation_list


def data_preprocess(text):    
    text  = text.lower()
    text = re.sub('\W+',' ', text)    
    return text
