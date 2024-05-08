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
# pattern = "У лінійного пошуку немає передумов до стану структури даних"
# pattern = "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"


# Для статті 2
# pattern = "Структура B+ tree показала результати, близькі до хеш-таблиці"
# pattern = "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"

cases = [["У лінійного пошуку немає передумов до стану структури даних", "Цього рядка не існує - Це підхід до хешування рядків, коли кожен символ рядка розглядається як коефіцієнт полінома"], ["СУБД типу NoSQL можуть бути реалізовані різними методами", "Цього рядка не існує - Визначено найшвидший алгоритм для кожного з двох текстів"]]


for case in cases:
    for pattern in case:
        position = kmp_search(main_string, pattern)
        if position != -1:
            print(f"Substring found at index {position}")
        else:
            print("Substring not found")

        time_taken = timeit.timeit(lambda: position)

        print("Time taken:", time_taken, "seconds")