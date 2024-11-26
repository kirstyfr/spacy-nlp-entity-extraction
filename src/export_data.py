import pandas as pd

def export_entities(model_name, abstract_unique_values, abstract_list_cleaned, abstract_file_name):
    # Convert the set of tuples to a list of dictionaries
    entities_list = [{'Model' : model_name, 'Data section': abstract_file_name, 'Article Count': len(abstract_list_cleaned), 'Article ID': id_, 'Entity': entity, 'Start': start, 'End': end} for id_, entity, start, end in abstract_unique_values]
    # Create a DataFrame from the list of dictionaries
    df_model_entities = pd.DataFrame(entities_list)
    # name csv file
    csv_file_name = f"{model_name}_{abstract_file_name}_{len(abstract_list_cleaned)}_entities_output"
    # Export the DataFrame to a CSV file
    df_model_entities.to_csv(f"/root/DS_Evidence/ds_project_folder/data/messy_outputs/{csv_file_name}.csv", index=False)
        
    
def export_performance(model_name, abstract_list_cleaned, annotation_unique_values, abstract_unique_values, num_common_elements, precision, recall, f1_score, abstract_file_name):
    # create row of data
    original_values_row = {
        'Model Name': model_name,
        'Dataset' : 'CHEMDNER',
        'Abstract count': len(abstract_list_cleaned),
        'Count entities extracted': len(abstract_unique_values), 
        'Count annotations' : len(annotation_unique_values), 
        'Count common elements':num_common_elements,
        'Precision' : precision,
        'Recall' : recall,
        'F1 Score' : f1_score,
        'Fuzzy Match Applied?' : 'no' ,
        'Character Difference' : 0,
        'Data section' : abstract_file_name,
        'ID' : f"{model_name}_{abstract_file_name}_{len(abstract_list_cleaned)}"
    }
    # Create the DataFrame
    df_performance = pd.DataFrame([original_values_row])
    # Export the Dataframe
    df_performance.to_csv('/root/DS_Evidence/ds_project_folder/data/processed_data/model_performance_metrics.csv', mode='a', header=False)

def export_entities_fuzzy(model_name, filtered_matches, abstract_list_cleaned, abstract_file_name):
        # Flatten the data
    flattened_data = []
    for entry in filtered_matches:
        flat_entry = entry.copy()
        best_match = flat_entry.pop('best_match')
        for k, v in best_match.items():
            flat_entry[f'best_match_{k}'] = v
        flattened_data.append(flat_entry)
    # Create a DataFrame from the flattened list of dictionaries
    df_fuzzy = pd.DataFrame(flattened_data)
    df_fuzzy['Model'] = model_name
    df_fuzzy['Article Count'] = len(abstract_list_cleaned)
    # Export the DataFrame to a CSV file
    csv_file_name_fuzzy = f"{model_name}_{abstract_file_name}_{len(abstract_list_cleaned)}_fuzzy_entities_output"
    # Export fuzzy matches to csv
    df_fuzzy.to_csv(f"/root/DS_Evidence/ds_project_folder/data/messy_outputs/{csv_file_name_fuzzy}.csv", index=False)
    
def export_performance_fuzzy(model_name, abstract_list_cleaned, annotation_unique_values, abstract_unique_values, num_common_elements_fuzzy, precision_fuzzy, recall_fuzzy, f1_score_fuzzy, char_diff, abstract_file_name):   
    # create row of data
    fuzzy_values_row = {
        'Model Name': model_name,
        'Dataset' : 'CHEMDNER',
        'Abstract count': len(abstract_list_cleaned),
        'Count entities extracted': len(abstract_unique_values), 
        'Count annotations' : len(annotation_unique_values), 
        'Count common elements':num_common_elements_fuzzy,
        'Precision' : precision_fuzzy,
        'Recall' : recall_fuzzy,
        'F1 Score' : f1_score_fuzzy,
        'Fuzzy Match Applied?' : 'yes' ,
        'Character Difference' : char_diff,
        'Data section' : abstract_file_name,
        'ID' : f"{model_name}_{abstract_file_name}_{len(abstract_list_cleaned)}"
}
    # Create the DataFrame
    df_fuzzy_performance = pd.DataFrame([fuzzy_values_row])
    # Append the performance metrics to csv
    df_fuzzy_performance.to_csv('/root/DS_Evidence/ds_project_folder/data/processed_data/model_performance_metrics.csv', mode='a', header=False)
    