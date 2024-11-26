import os
import sys

# Navigate up two levels to reach src directory
src_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(src_path)

# Standard imports
import os
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Custom imports
from src.entity_extraction import Extractor
from src.load_data import *
from src.wordcloud import generate_wordcloud
from src.evaluation_metrics import *
from src.text_preprocessing import data_preprocess
from src.export_data import export_entities, export_performance
from src.fuzzy_matching import fuzzy_match
from src.export_data import  export_entities_fuzzy, export_performance_fuzzy
