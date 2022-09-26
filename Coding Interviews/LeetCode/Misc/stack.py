class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)
    
    def pop(self):
        return self.elements.pop()

stack = Stack()
stack.push(7)
stack.push(8)
print(stack.pop())
print(stack.pop())

x = "1 2 3 4\n"
hello = x.strip('\n')
hello = hello.split(" ")
print(hello)
print(hello[-1].split("\\"))