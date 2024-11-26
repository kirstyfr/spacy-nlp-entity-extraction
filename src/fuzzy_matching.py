from fuzzywuzzy import fuzz

def fuzzy_match(abstract_unique_values, annotation_unique_values, char_diff):
    # Initialize counter
    rows_processed = 0
    matches_per_entity = []

    # Iterating through extract list to extract its closest match from the annotation list
    for article, entity, start, end in abstract_unique_values:
        # Increment the counter
        rows_processed += 1
        
        # Print the current count without clearing the output
        print(f"Rows processed: {rows_processed}", end='\r')

        best_match = None
        highest_ratio = 0
        
        for annotation_article, annotation_entity, annotation_start, annotation_end in annotation_unique_values:
            # Calculate similarity ratio based on substring within specified range
            ratio = fuzz.ratio(entity, annotation_entity)
            if ratio > highest_ratio and article == annotation_article and abs(start - annotation_start) <= char_diff and abs(end - annotation_end) <= char_diff:
                highest_ratio = ratio
                best_match = {
                    'annotation_article': annotation_article,
                    'annotation_entity': annotation_entity,
                    'similarity_ratio': highest_ratio,
                    'annotation_start': annotation_start,
                    'annotation_end': annotation_end
                }
                # Break out of the loop once a match is found
                break

        matches_per_entity.append({
            'article': article,
            'entity': entity,
            'start': start,
            'end': end,
            'best_match': best_match,
            'highest_ratio': highest_ratio 
        })                

    print(f"\nTotal rows processed: {rows_processed}")
    
    # Filter out entries where best_match is None
    filtered_matches = [match for match in matches_per_entity if match['best_match'] is not None]
    
    
    return filtered_matches, matches_per_entity, char_diff
