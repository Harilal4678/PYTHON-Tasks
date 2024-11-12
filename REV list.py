def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list


original_list = [1, 2, 3, 4, 5]
reversed_result = reverse_list(original_list)
print("Original List:", original_list)
print("Reversed List:", reversed_result)
