import random
import string

import population

random1 = random.randint (1000000000, 9999999999)
print(random1)

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

random_word = generate_random_word(8)  # Генерировать случайное слово длиной 8 символов
print(random_word)

word_list = ["apple", "banana", "orange", "grape", "pineapple"]

def generate_random_existing_word(word_list):
    return random.choice(word_list)

random_existing_word = generate_random_existing_word(word_list)
print(random_existing_word)

expire_date = "2412"
reversed_expire_date = expire_date[2:] + expire_date[:2]
print(reversed_expire_date)  # Вывод: 1224