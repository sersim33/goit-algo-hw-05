#Алгоритм Боєра-Мура
import requests
import timeit

def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
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
for function in [boyer_moore_search]:
    for article in cases:
        for substring in article[1]:
            measure_time(function, article[0], substring)