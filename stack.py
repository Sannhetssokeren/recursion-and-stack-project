class Stack:
    def __init__(self):
        """
        Инициализирует пустой стек.
        """
        self.items = []

    def push(self, item):
        """
        Добавляет элемент в стек.

        :param item: Элемент, который нужно добавить.
        """
        self.items.append(item)

    def pop(self):
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Верхний элемент стека.
        :raises IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Стек пуст.")
        return self.items.pop()

    def peek(self):
        """
        Возвращает верхний элемент стека без его удаления.

        :return: Верхний элемент стека.
        :raises IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Стек пуст.")
        return self.items[-1]

    def is_empty(self):
        """
        Проверяет, пуст ли стек.

        :return: True, если стек пуст, иначе False.
        """
        return len(self.items) == 0