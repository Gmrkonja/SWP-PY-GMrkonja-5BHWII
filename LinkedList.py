import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def __len__(self):
        return self.size

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

def main():
    linked_list = LinkedList()
    for _ in range(10):
        linked_list.append(random.randint(1, 100))
    
    print("Länge der Liste:", len(linked_list))
    print("Elemente der Liste:", linked_list.display())
    print("Jedes einzelne Element.")
    current = linked_list.head
    while current:
        print(current.value, end=" ")
        current = current.next

if __name__ == "__main__":
    main()
