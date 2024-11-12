def find_maximum(numbers):
    if not numbers:  # Check if the list is empty
        return None
    
    maximum = numbers[0]  # Assume the first element is the maximum initially
    for num in numbers:
        if num > maximum:
            maximum = num  # Update maximum if a larger number is found
    return maximum

# Example usage
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print("The maximum number is:", find_maximum(numbers_list))
