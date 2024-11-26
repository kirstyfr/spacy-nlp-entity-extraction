from sklearn.metrics import confusion_matrix
import numpy as np

def calculate_evaluation_metrics(annotation_list, abstract_list):
    annotation_unique_values = {((item[0]),) + item[1] for item in annotation_list}
    abstract_unique_values = {(item[0],)+ subitem[0:1]+subitem[2:4] for item in abstract_list for subitem in item[1]}

    intersection = annotation_unique_values.intersection(abstract_unique_values)

    num_common_elements = len(intersection)
    num_annotations_unique = len(annotation_unique_values)
    num_abstract_unique = len(abstract_unique_values)
    ######################### swap precision and recall
    recall = num_common_elements / num_annotations_unique if num_annotations_unique != 0 else 0
    precision = num_common_elements / num_abstract_unique if num_abstract_unique != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    
    return num_common_elements, precision, recall, f1_score, annotation_unique_values, abstract_unique_values, intersection

def print_evaluation_metrics(annotation_list_cleaned, abstract_list_cleaned, abstract_ids):
    # Calculate evaluation metrics
    num_common_elements, precision, recall, f1_score, annotation_unique_values, abstract_unique_values, intersection = calculate_evaluation_metrics(annotation_list_cleaned, abstract_list_cleaned)
    
    # Prepare the metrics for printing
    metrics = {
        "Number of abstracts scanned": len(abstract_ids),
        "Number of entities extracted": len(abstract_unique_values),
        "Number of annotations in dataset": len(annotation_unique_values),
        "Number of common elements": num_common_elements,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1_score
    }
    
    # Print evaluation metrics using formatted strings
    for key, value in metrics.items():
        print(f"{key}: {value}")

    return num_common_elements, precision, recall, f1_score


def calculate_evaluation_metrics_with_fuzzy(annotation_list, abstract_list, filtered_matches):
    annotation_unique_values = {((item[0]),) + item[1] for item in annotation_list}
    abstract_unique_values = {(item[0],)+ subitem[0:1]+subitem[2:4] for item in abstract_list for subitem in item[1]}

    num_common_elements_fuzzy = len(filtered_matches)
    num_annotations_unique = len(annotation_unique_values)
    num_abstract_unique = len(abstract_unique_values)

    recall_fuzzy = num_common_elements_fuzzy / num_annotations_unique if num_annotations_unique != 0 else 0
    precision_fuzzy = num_common_elements_fuzzy / num_abstract_unique if num_abstract_unique != 0 else 0
    f1_score_fuzzy = 2 * (precision_fuzzy * recall_fuzzy) / (precision_fuzzy + recall_fuzzy) if (precision_fuzzy + recall_fuzzy) != 0 else 0

    return num_common_elements_fuzzy, precision_fuzzy, recall_fuzzy, f1_score_fuzzy


def print_fuzzy_evaluation_metrics(annotation_list_cleaned, abstract_list_cleaned, filtered_matches, abstract_ids, abstract_unique_values,annotation_unique_values):
    # Calculate evaluation metrics with fuzzy matches
    num_common_elements_fuzzy, precision_fuzzy, recall_fuzzy, f1_score_fuzzy = calculate_evaluation_metrics_with_fuzzy_new(annotation_list_cleaned, abstract_list_cleaned, filtered_matches)
    
    
    metrics = {
        "Number of abstracts scanned": len(abstract_ids),
        "Number of entities extracted": len(abstract_unique_values),
        "Number of annotations in dataset": len(annotation_unique_values),
        "Number of common elements": num_common_elements_fuzzy,
        "Precision": precision_fuzzy,
        "Recall": recall_fuzzy,
        "F1 Score": f1_score_fuzzy
    }
    
    # Print evaluation metrics using formatted strings
    for key, value in metrics.items():
        print(f"{key}: {value}")


