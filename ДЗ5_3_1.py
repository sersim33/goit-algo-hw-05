#Рабіна-Карпа

import requests
import timeit

def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

# URL-адреса файлу на Google Drive
# url = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"

# (стаття 2)
url = "https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"

# Виконуємо запит для отримання вмісту файлу
response = requests.get(url)

# Перевіряємо, чи був успішний запит
if response.status_code == 200:
    # Отримуємо вміст файлу
    code = response.text

main_string = code
# substring = "У лінійного пошуку немає передумов до стану структури даних"
# substring = "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"

# Для статті 2
# substring = "СУБД типу NoSQL можуть бути реалізовані різними методами"
# substring = "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"

cases = [["У лінійного пошуку немає передумов до стану структури даних", "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"], ["СУБД типу NoSQL можуть бути реалізовані різними методами", "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"]]


for case in cases:
    for substring in case:
        position = rabin_karp_search(main_string, substring)
        if position != -1:
            print(f"Substring found at index {position}")
        else:
            print("Substring not found")

        time_taken = timeit.timeit(lambda: position)

        print("Time taken:", time_taken, "seconds")