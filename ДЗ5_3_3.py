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


# URL-адреса файлу на Google Drive
# url = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"

# (стаття 2)
url  = "https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"

# Виконуємо запит для отримання вмісту файлу
response = requests.get(url)

# Перевіряємо, чи був успішний запит
if response.status_code == 200:
    # Отримуємо вміст файлу
    code = response.text

text = code

# pattern = "У лінійного пошуку немає передумов до стану структури даних"
# pattern = "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"

# Для статті 2
# pattern = "Структура B+ tree показала результати, близькі до хеш-таблиці"
#  pattern = "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"

cases = [["У лінійного пошуку немає передумов до стану структури даних", "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"], ["СУБД типу NoSQL можуть бути реалізовані різними методами", "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"]]
for case in cases:
    for pattern in case:
        position = boyer_moore_search(text, pattern)
        if position != -1:
            print(f"Substring found at index {position}")
        else:
            print("Substring not found")

        time_taken = timeit.timeit(lambda: position)

        print("Time taken:", time_taken, "seconds")