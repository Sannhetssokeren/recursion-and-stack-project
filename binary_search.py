def binary_search_recursive(arr, target, left=0, right=None):
    """
    Выполняет рекурсивный бинарный поиск элемента в отсортированном списке.

    :param arr: Отсортированный список.
    :param target: Элемент, который нужно найти.
    :param left: Левая граница поиска.
    :param right: Правая граница поиска.
    :return: Индекс элемента, если он найден, или -1, если элемент не найден.
    """
    if right is None:
        right = len(arr) - 1

    if left > right:  # Базовый случай: элемент не найден
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:  # Базовый случай: элемент найден
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)