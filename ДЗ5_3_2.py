#Кнута-Морріса-Пратта

import requests
import timeit

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

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
for function in [kmp_search]:
    for article in cases:
        for substring in article[1]:
            measure_time(function, article[0], substring)
