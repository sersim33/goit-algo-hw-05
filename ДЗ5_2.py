def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == x:
            return iterations, arr[mid]
        elif arr[mid] < x:
            low = mid + 1
            if low < len(arr):
                upper_bound = arr[low]
        else:
            high = mid - 1
            if high >= 0:
                upper_bound = arr[mid]

    return iterations, upper_bound

# Приклад використання
arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
x_values = [0.5, 0.78]

# порівняємо різні значення 
for x in x_values:
  print(binary_search(arr, x))