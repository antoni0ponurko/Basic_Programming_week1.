def remove_duplicates(input_list):
    
    unique_elements = set(input_list)  
    
    return list(unique_elements)  

original_list = ['A', 89, 78, 4, 'A', 'test', 4]

new_list = remove_duplicates(original_list)

print(f"Original list: {original_list}")
print(f"Without duplicates: {new_list}")
