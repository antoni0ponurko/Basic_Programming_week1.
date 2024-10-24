def give_even_positions(input_list):
    
    even_position_elements = [input_list[i] for i in range(len(input_list)) if i % 2 == 0]
    
    return even_position_elements

original_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

even_positions_list = give_even_positions(original_list)

print(f"Original list: {original_list}")
print(f"The elements in the even positions are: {even_positions_list}")
