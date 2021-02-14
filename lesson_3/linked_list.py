from typing import Any, Sequence, Optional


class LinkedList:
    class Node:
        """
        Внутренний класс, класса LinkedList.

        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """
        def __init__(self, value: Any, next_: Optional['Node'] = None):
            """
            Создаем новый узел для односвязного списка

            :param value: Любое значение, которое помещено в узел
            :param next_: следующий узел, если он есть
            """
            self.value = value
            self.next = next_  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional['Node']):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head = None  # Node
        self.tail = None

        if data:  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{[value for value in self]}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"{type(self).__name__}({[value for value in self]})"

    def __len__(self) -> int:
        return self.__len

    def __step_by_step_on_nodes(self, index) -> 'Node':
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.__len:
            raise IndexError()
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, item: int) -> Any:
        current_node = self.__step_by_step_on_nodes(item)
        return current_node.value

    def __setitem__(self, key: int, value: Any):
        current_node = self.__step_by_step_on_nodes(key)
        current_node.value = value

    # def append_1(self, value: Any):
    #     """Добавление элемента в конец связного списка"""
    #     append_node = self.Node(value)
    #     if self.head is None:
    #         self.head = append_node
    #     else:
    #         tail = self.head  # ToDo Завести атрибут self.tail, который будет хранить последний узел
    #         for _ in range(self.__len - 1):
    #             tail = tail.next
    #         self.__linked_nodes(tail, append_node)
    #     self.__len += 1

    def append(self, value: Any):
        append_node = self.Node(value)
        if self.head == None:
            self.head = append_node
        if self.tail != None:
            self.tail.next = append_node
        self.tail = append_node
        self.__len += 1


    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        if index == 0:
            insert_node = self.Node(value)
            self.__linked_nodes(insert_node, self.head)
            self.head = insert_node
            self.__len += 1
        elif 1 <= index < self.__len:
            prev_node = self.__step_by_step_on_nodes(index - 1)
            current_node = prev_node.next
            insert_node = self.Node(value, next_=current_node)
            self.__linked_nodes(prev_node, insert_node)
            self.__len += 1
        elif index >= self.__len:
            self.append(value)

    def clear(self) -> None:
        self.head = None
        self.__len = 0

    def index(self, value: Any) -> int:
        current_node = self.head
        for i in range(self.__len):
            if str(current_node) == value:
                return i
            else:
                current_node = current_node.next
        raise ValueError(f'{value} is not in list')

    def remove(self, value: Any) -> None:
        current_index = self.index(value)
        if current_index == 0:
            self.head = self.__step_by_step_on_nodes(1)
            self.__len -= 1
        elif 1 <= current_index < self.__len:
            prev_node = self.__step_by_step_on_nodes(current_index - 1)
            prev_node.next = prev_node.next.next
            # next_node = self.__step_by_step_on_nodes(current_index + 1)
            # self.__linked_nodes(prev_node, next_node)
            self.__len -= 1
        elif current_index + 1 == self.__len:
            prev_node = self.__step_by_step_on_nodes(current_index - 1)
            prev_node.next = None
            self.__len -= 1

    def sort(self) -> None:
        for i in range(self.__len):
            current_index = 0
            current_node = self.__step_by_step_on_nodes(current_index)
            current_value = current_node.value
            next_node = self.__step_by_step_on_nodes(current_index + 1)
            next_value = next_node.value
            for current_index in range(self.__len - 1):
                if current_value > next_value:
                    current_node.value = next_value
                    next_node.value = current_value
                current_node = self.__step_by_step_on_nodes(current_index)
                current_value = current_node.value
                next_node = self.__step_by_step_on_nodes(current_index + 1)
                next_value = next_node.value
            if current_value > next_value:
                current_node.value = next_value
                next_node.value = current_value

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        if hasattr(data, '__iter__'):
            return True
        else:
            raise AttributeError(f'{data.__class__.__name__} is not iterable')


if __name__ == '__main__':
    # ll = LinkedList([1, 2, 3, 4])
    # print(ll)

    l1 = LinkedList('')
    l1.append('8')
    print(l1)
    # l1.sort()
    # print(l1)
    # l1.insert(0, 'value')
    # print(l1)
    # l1.insert(len(l1)-1, 'new_value')
    # print(l1)



