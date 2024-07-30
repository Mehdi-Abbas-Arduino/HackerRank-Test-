def stringAnagram(dictionary, query):
    from collections import Counter
    
    # Normalize dictionary words by sorting their characters
    sorted_dict = [''.join(sorted(word)) for word in dictionary]
    
    # Count occurrences of each sorted word
    dict_count = Counter(sorted_dict)
    
    # Initialize result list
    result = []
    
    # For each query, find its sorted version and count in the dictionary
    for q in query:
        sorted_q = ''.join(sorted(q))
        result.append(dict_count.get(sorted_q, 0))
    return result