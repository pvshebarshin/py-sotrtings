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
