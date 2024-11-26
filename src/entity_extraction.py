import spacy
from spacy.language import Language
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

class Extractor:
    def __init__(self):
        self.model = None  # Initialize model attribute
        self.model_name = None  # Add an attribute to store max_rows
        self.max_rows = None  # Add an attribute to store max_rows
    
    def load_model(self, model_name="en_ner_bc5cdr_md"):
        if model_name == 'en_core_sci_scibert':
            self.tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
            self.model = pipeline('ner', model=AutoModelForTokenClassification.from_pretrained('allenai/scibert_scivocab_uncased'), tokenizer=self.tokenizer)
        else:
            self.model = spacy.load(model_name)
        self.model_name = model_name
        return self.model
            
        return self.model
    
    def get_model_name(self):
        return self.model_name
    
    def get_max_rows(self):
        return self.max_rows
    
    def extract_entities(self, text, tokenizer=None, max_length=512):
            if self.model is None:
                raise ValueError("Model has not been loaded. Call load_model() first.")
        
        # Check if the model is SciBERT
            if self.model_name == 'en_core_sci_scibert':
                if tokenizer is None:
                    raise ValueError("Tokenizer is required for SciBERT model. Pass the tokenizer as an argument.")
            
            # Tokenize the text using the provided tokenizer
                tokenized_text = tokenizer.encode(text, padding=True, truncation=True, max_length=max_length, add_special_tokens=True)
            
            # Convert the token IDs back to text
                tokens = tokenizer.convert_ids_to_tokens(tokenized_text)
                truncated_text = tokenizer.decode(tokenized_text)
            
            # Process the truncated text with the model
                doc = self.model(truncated_text)
                
                # Extract entities
                entities = [(entity['word'], entity['entity'], entity['start'], entity['end']) for entity in doc]
            
                return entities
            
            else:
            # Process text with the regular model
                doc = self.model(text)
        
            return [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]
        
class Extractor_BERT:
    def __init__(self):
        self.model = None  # Initialize model attribute
        self.model_name = None  # Add an attribute to store max_rows
        self.max_rows = None  # Add an attribute to store max_rows
    
    def load_model(self, model_name="en_ner_bc5cdr_md"):
        if self.model is None:
            self.model = spacy.load(model_name)
            self.model_name = model_name  
            
        return self.model
    
    def get_model_name(self):
        return self.model_name
    
    def get_max_rows(self):
        return self.max_rows    
    
    def extract_entities(self, text, tokenizer=AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased"), max_length=512):
            if self.model is None:
                raise ValueError("Model has not been loaded. Call load_model() first.")
        
        # Check if the model is SciBERT
            if self.model_name == 'en_core_sci_scibert':
                if tokenizer is None:
                    raise ValueError("Tokenizer is required for SciBERT model. Pass the tokenizer as an argument.")
            
            # Tokenize the text using the provided tokenizer
                tokenized_text = tokenizer.encode(text, padding=True, truncation=True, max_length=max_length, add_special_tokens=True)
            
            # Convert the token IDs back to text
                tokens = tokenizer.convert_ids_to_tokens(tokenized_text)
                truncated_text = tokenizer.decode(tokenized_text)
            
            # Process the truncated text with the model
                doc = self.model(truncated_text)
            
            else:
            # Process text with the regular model
                doc = self.model(text)
        
            return [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]

    
  


