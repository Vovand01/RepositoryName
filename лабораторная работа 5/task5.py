from string import ascii_lowercase, ascii_uppercase, digits
from random import sample
def get_random_password(number_of_symbols=8) -> str:
    password = sample(ascii_lowercase + ascii_uppercase + digits, number_of_symbols)
    return "".join(password)
print(get_random_password())
