# Stack is a linear data structure that follows LIFO(last in first out) principle, 
# the last element inserted is the first to be popped out. 

# list implementation of stack

# li1 = []

# li1.append(5)
# li1.append(8)
# li1.append(56)
# li1.append(50)
# li1.append(20)
# print(li1)

# li1.pop()
# print(li1)

class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.insert(0, value)

    def peek(self):       # dekhne ke liye
        if len(self.s) == 0:
            raise Exception("stack is empty")
        else:
            return self.s[0]
    def pop(self):
        return self.s.pop(0)  # index 0
    
stk = stack()
stk.push(55)
stk.push(85)
stk.push(5)

print(stk.peek())   # last index dekhne ke liye
# print(stk())

print(stk.peek())

print(stk.pop())

print(stk.s)