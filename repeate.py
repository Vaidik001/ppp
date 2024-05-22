#python program that removes any repeated items from a list so that each item appears at most once.
# For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

def remove_duplicates(input_list):
    return list(set(input_list))

# Example usage
original_list = [1, 1, 2, 3, 4, 3, 0, 0]
unique_list = remove_duplicates(original_list)
print(unique_list)



def remove_duplicates_preserve_order(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# Example usage
original_list = [1, 1, 2, 3, 4, 3, 0, 0]
unique_list = remove_duplicates_preserve_order(original_list)
print(unique_list)