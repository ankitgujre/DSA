# Linked list is basically cain of nodes where each nodes contains information such as data 
# a pointer to the next node in the chain

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# a = Node(5)
# b = Node(3)
# c = Node(7)

# a.next = b
# b.next = c

# head = a

# print(head.data)
# print(head.next.data)

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # Delete a node
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None


    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Create Linked List
ll = LinkedList()

ll.insert_begin(10)
ll.insert_begin(5)

ll.insert_end(20)
ll.insert_end(30)

print("Linked List:")
ll.display()

ll.delete(20)

print("After deleting 20:")
ll.display()


