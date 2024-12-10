import random

from python.utils import is_sorted

MIN_MERGE = 32


def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1

    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
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

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1] and i + 1 < n:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1] and i + 1 < n:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr


def bozo_sort(arr):
    while not is_sorted(arr):
        i = random.randint(0, len(arr) - 1)
        j = random.randint(0, len(arr) - 1)

        arr[i], arr[j] = arr[j], arr[i]
    return arr


def __permute(arr):
    if len(arr) == 0:
        return [[]]
    if len(arr) == 1:
        return [arr]

    permutations = []

    # Генерируем перестановки
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i + 1:]

        for p in __permute(remaining):
            permutations.append([current] + p)

    return permutations


def perm_sort(arr):
    # Генерируем все возможные перестановки
    permutations = __permute(arr)

    # Находим минимальную перестановку (отсортированный массив)
    sorted_arr = min(permutations)

    return sorted_arr


def __stooge_sort(arr, l, r):
    # Если первый элемент больше последнего, меняем их местами
    if arr[l] > arr[r]:
        arr[l], arr[r] = arr[r], arr[l]

    # Если размер массива больше 2
    if r - l + 1 > 2:
        t = r - l + 1
        __stooge_sort(arr, l, r - t // 3)
        __stooge_sort(arr, l + t // 3, r)
        __stooge_sort(arr, l, r - t // 3)


def stooge_sort(arr):
    __stooge_sort(arr, 0, len(arr) - 1)
    return arr


def merge_sort(arr):
    __merge_sort(arr)
    return arr


def __merge_sort(arr):
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


def __heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        __heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        __heapify(arr, i, 0)


def __heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        __heapify(arr, n, largest)


def heap_sort(arr):
    __heap_sort(arr)
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def shell_sort(arr):
    n = len(arr)
    step = n // 2

    while step > 0:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp
        step //= 2
    return arr


def shaker_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    _sorted = False

    while not _sorted:
        _sorted = True
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False

        right -= 1

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                _sorted = False
        left += 1
    return arr


def __compare_and_swap(arr, i, j, direction):
    if (direction == 1 and arr[i] > arr[j]) or (direction == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]


def __bitonic_merge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            __compare_and_swap(arr, i, i + k, direction)
        __bitonic_merge(arr, low, k, direction)
        __bitonic_merge(arr, low + k, k, direction)


def __bitonic_sort(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        __bitonic_sort(arr, low, k, 1)
        __bitonic_sort(arr, low + k, k, 0)
        __bitonic_merge(arr, low, cnt, direction)


def bitonic_sort(arr):
    n = len(arr)
    if n & (n - 1) != 0:
        raise ValueError("Длина массива должна быть степенью двойки.")
    __bitonic_sort(arr, 0, n, 1)
    return arr


def __calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def __insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def __merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)
    min_run = __calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        __insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:  # There is a run to merge
                left_run = arr[left:mid + 1]
                right_run = arr[mid + 1:right + 1]
                __merge(left_run, right_run, arr[left:right + 1])

        size *= 2
    return arr


def __flip(arr, k):
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1


def __find_max_index(arr, n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index


def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = __find_max_index(arr, curr_size)

        if max_index != curr_size - 1:
            __flip(arr, max_index)
            __flip(arr, curr_size - 1)
    return arr


def cycle_sort(arr):
    n = len(arr)

    writes = 0

    for index in range(0, n - 1):
        temp = arr[index]
        pos = index
        for i in range(index + 1, n):
            if arr[i] < temp:
                pos += 1

        if pos == index:
            continue

        while temp == arr[pos]:
            pos += 1

        if pos != index:
            t = temp
            temp = arr[pos]
            arr[pos] = t
            writes += 1

        while pos != index:
            pos = index

            for j in range(index + 1, n):
                if arr[j] < temp:
                    pos += 1

            while temp == arr[pos]:
                pos += 1

            if temp != arr[pos]:
                t = temp
                temp = arr[pos]
                arr[pos] = t
                writes += 1
    return arr
