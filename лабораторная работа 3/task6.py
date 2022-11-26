list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
max_element = list_numbers[max_index]
for element_number, value in enumerate(list_numbers):
    max_element = list_numbers[max_index]
    if value >= max_element:
        max_index = element_number
        max_element = list_numbers[max_index]
list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
