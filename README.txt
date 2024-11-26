README for ScispaCy Biomedical Entity Extraction Notebook

**IMPORTANT***Use main_notebook as the main notebook for this project as it contains the majority of the entity extraction models- sciBERT_WORKFLOW is for the SciBERT model only.

Overview
--------
This notebook is designed for evaluating and extracting biomedical entities using various pre-trained models from SciSpacy. The workflow includes loading models, processing abstracts, running performance metrics, and exporting results. The notebook also supports fuzzy matching to improve entity extraction accuracy.

Available Models
----------------
You can choose from the following pre-trained models:

- en_ner_bc5cdr_md: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz
- en_core_sci_md: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.3/en_core_sci_md-0.5.3.tar.gz
- en_core_sci_sm: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.3/en_core_sci_sm-0.5.3.tar.gz
- en_ner_bionlp13cg_md: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bionlp13cg_md-0.5.4.tar.gz
- en_ner_jnlpba_md: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_jnlpba_md-0.5.4.tar.gz
- en_ner_craft_md: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_craft_md-0.5.4.tar.gz
- en_core_sci_lg: https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_lg-0.5.4.tar.gz

For using SciBERT, refer to the 2_sciBERT_WORKFLOW.ipynb notebook and replace the load_model and pip install steps accordingly.

Installation
------------
To use the notebook, install the required model and additional packages:

pip install -q https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_lg-0.5.4.tar.gz
pip install wordcloud
pip install fuzzywuzzy
pip install nltk --quiet
pip install transformers -U

Usage
-----
1. Import Modules:
   from imports import *

2. Initialize Extractor:
   extractor = Extractor()

3. Load the Model:
   Select the model you want to use:
   extractor.load_model('en_core_sci_lg')

4. Select CHEMDNER data section and the amount of abstracts to pass through model viamax_rows, load abstracts and clean data, 

   abstract_list_cleaned, abstract_ids, abstract_file_name = load_abstracts_clean_data_name('evaluation.abstracts', extractor, max_rows=1000, clean_data=True)

5. Store Model Name:
   model_name = extractor.get_model_name()

6. Load cleaned/reformatted Annotations:
   annotation_list_cleaned = load_annotations('/root/DS_Evidence/ds_project_folder/data/raw_data/CHEMNER/evaluation.annotations.txt', abstract_ids, clean_data=True)

7. Run Performance Metrics on initial entity extraction:
   num_common_elements, precision, recall, f1_score, annotation_unique_values, abstract_unique_values, intersection = calculate_evaluation_metrics(annotation_list_cleaned, abstract_list_cleaned)

8. Print Performance Metrics:
   print_evaluation_metrics(annotation_list_cleaned, abstract_list_cleaned, abstract_ids)

9. Export Entities as csv:
   export_entities(model_name, abstract_unique_values, abstract_list_cleaned, abstract_file_name)

10. Append Performance Metrics to existing csv:
    export_performance(model_name, abstract_list_cleaned, annotation_unique_values, abstract_unique_values, num_common_elements, precision, recall, f1_score, abstract_file_name)

11. Run Fuzzy Match and Select Character Limit:
    filtered_matches, matches, char_diff = fuzzy_match(abstract_unique_values, annotation_unique_values, 10)

12. Re-calculate Evaluation Metrics with Fuzzy Matches:
    num_common_elements_fuzzy, precision_fuzzy, recall_fuzzy, f1_score_fuzzy = calculate_evaluation_metrics_with_fuzzy_new(annotation_list_cleaned, abstract_list_cleaned, filtered_matches)

13. Print Fuzzy Evaluation Metrics:
    print_fuzzy_evaluation_metrics(annotation_list_cleaned, abstract_list_cleaned, filtered_matches, abstract_ids, abstract_unique_values, annotation_unique_values)

14. Export Fuzzy Match Entities as csv:
    export_entities_fuzzy(model_name, filtered_matches, abstract_list_cleaned, abstract_file_name)

15. Append Fuzzy Performance Metrics to csv:
    export_performance_fuzzy(model_name, abstract_list_cleaned, annotation_unique_values, abstract_unique_values, num_common_elements_fuzzy, precision_fuzzy, recall_fuzzy, f1_score_fuzzy, char_diff, abstract_file_name)

src Directory Files
-------
- imports.py: Manages the imports for the project, including standard and custom imports. It helps in setting up the environment and importing necessary modules and functions from other scripts in the src directory.
- entity_extraction.py: Contains the Extractor class used for loading models and extracting entities from text. It supports different models, including SciSpacy and SciBERT.
- evaluation_metrics.py: Provides functions to calculate and print evaluation metrics such as precision, recall, and F1 score, helping assess the performance of the entity extraction models.
- export_data.py: Contains functions to export the extracted entities and performance metrics to CSV files for further analysis and record-keeping.
- fuzzy_matching.py: Implements the fuzzy_match function to perform fuzzy matching between extracted entities and annotations, improving the accuracy of entity extraction.
- load_data.py: Handles loading and cleaning data, including abstracts and annotations, preparing them for processing and evaluation.
- text_preprocessing.py: Includes functions for preprocessing text data, such as tokenization and stopword removal, to clean and prepare the text for analysis.
- wordcloud.py: Generates word clouds from the extracted entities, providing a visual representation of the most common terms and entities in the dataset.

Data
-----
- raw_data contains all the source development, evaluation and training CHEMDNER datasets and annotations used by the models
- messy_outputs contains all the intial entities and their closest fuzzy match outputted by the models
- processed_data contains all the formatted performance metrics for each model and data set
_ cleaned_abstracts_annotations is the formatted/cleaned version of the CHEMDNER datasets before they go through the entity extraction process


Notes
-----
- Ensure to replace the load_model step and install the appropriate package if you are using SciBERT by following the 2_sciBERT_WORKFLOW.ipynb.
- Select the number of abstracts to run through the model via max_rows and select the subsection of CHEMDNER data in the load_abstracts function
