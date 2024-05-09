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
    """
    Повертає позицію підрядка у вихідному рядку або -1, якщо підрядок не знайдено.
    """
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus

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

def get_text(url):
    """
    Отримує текстовий вміст за URL-адресою.
    """
    response = requests.get(url)
    try:
        response.raise_for_status()
        # print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        # print("Error fetching content:", e)
        return ""

def measure_time(func, text, substring, iterations=100):
    """
    Вимірює час виконання функції середньо за вказану кількість ітерацій.
    """
    setup = f'from __main__ import {func.__name__}; text = """{text}"""; substring = """{substring}"""'
    stmt = f'{func.__name__}(text, substring)'
    time_taken = timeit.timeit(stmt=stmt, setup=setup, number=iterations)
    print(f"Average time taken for {func.__name__}: {time_taken} seconds")


url1 = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"  # Стаття 1
url2 = "https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"  # Стаття 2

main_text1 = get_text(url1)
main_text2 = get_text(url2)

# Підрядки для пошуку
substring_1_t = "Автори публiкації"
substring_1_f = "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"
substring_2_t = "СУБД типу NoSQL можуть бути реалізовані різними методами"
substring_2_f = "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"

# Список варіантів для аналізу
cases = [(main_text1, [substring_1_t, substring_1_f]), (main_text2, [substring_2_t, substring_2_f])]

# Вимірюємо час виконання для кожної функції та кожного варіанту
for function in [rabin_karp_search]:
    for article in cases:
        for substring in article[1]:
            measure_time(function, article[0], substring)

#
length_article1 = len(main_text1)
length_article2 = len(main_text2)

print("Length of article 1:", length_article1)
print("Length of article 2:", length_article2)