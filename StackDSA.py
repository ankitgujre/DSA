# Stack is a linear data structure that follows LIFO(last in first out) principle, 
# the last element inserted is the first to be popped out. 

# list implementation of stack

li1 = []

li1.append(5)
li1.append(8)
li1.append(56)
li1.append(50)
li1.append(20)
print(li1)

li1.pop()
print(li1)

class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    