from random import randint
def get_unique_list_numbers(number_of_numbers=15, start=-10, stop=10) -> list[int]:
    list_ = []
    while len(list_) < number_of_numbers:
        number = randint(start, stop)
        if number not in list_:
            list_.append(number)
    return list_
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
