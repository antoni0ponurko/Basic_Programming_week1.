def max_en_min_uit_list(collection):
    
    max_value = max(collection)
    min_value = min(collection)
    
    return f"From {collection} is the max: {max_value} and min: {min_value}"

numbers = [11, 52, 125, -89, 1245]
print(max_en_min_uit_list(numbers))

words = ['jan', 'feb', 'mar', 'apr', 'may']
print(max_en_min_uit_list(words))
