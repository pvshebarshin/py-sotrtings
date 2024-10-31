import random

from python.utils import is_sorted


def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # Находим максимальное значение в массиве
    max_val = max(arr)

    # Создаем массив для подсчета вхождений
    count = [0] * (max_val + 1)

    # Подсчитываем вхождения каждого элемента
    for num in arr:
        count[num] += 1

    # Формируем отсортированный массив
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1

    return arr


def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем их местами, если они в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)  # Случайно перемешиваем массив
    return arr


def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        # Сортировка по четным индексам
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1] and i + 1 < n:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        # Сортировка по нечетным индексам
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1] and i + 1 < n:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Левая половина
        right_half = arr[mid:]  # Правая половина

        merge_sort(left_half)  # Рекурсивно сортируем левую половину
        merge_sort(right_half)  # Рекурсивно сортируем правую половину

        i = j = k = 0

        # Слияние подмассивов
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы в левой половине
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Проверяем, остались ли элементы в правой половине
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1