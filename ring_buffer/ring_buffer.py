from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current:
            if self.current == self.capacity:
                self.current = None
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current is None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = 1
            else:
                location = self.storage.head
                i = 0
                while location:
                    if location.value:
                        if i == self.current:
                            location.value = item
                            self.current += 1
                            break
                        location = location.next
                    i += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        start = self.storage.head
        while start:
            if start.value:
                list_buffer_contents.append(start.value)
                start = start.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def __len__(self):
        return self.capacity


    def append(self, item):
        if self.current == self.capacity:
            self.current = 0

        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        index = len(self.storage)
        for i in range(len(self.storage)):
            if self.storage[i] is None:
                index = i
        return self.storage[:index]


test = ArrayRingBuffer(3)
test.append('a')
test.append('b')
test.append('c')
test.append('d')
print(test.get())
