###Q1. Stack Implementation:LIFO
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0 :
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def reverse(self):
        self.items.reverse()

    def clear(self):
        self.items = []

    def show(self):
        print("Full Stack:", self.items)

#Example usage:
stack = Stack()
# print("Popped Element:", stack.pop())
# print("Top Element:", stack.peek())

stack.push("Horse")
stack.push("Dog")
stack.push("Zebra")
print(stack.is_empty())

stack.show()
print("Stack Size:", stack.size())
print("Top Element:", stack.peek())
print("Popped Element:", stack.pop())
stack.show()

stack.clear()
stack.show()
print(stack.is_empty())

print()

###Q1. Queue Implementation:FIFO
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0 :
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from empty queue")

    def get_rear(self):
            if not self.is_empty():
                return self.items[-1]
            else:
                raise IndexError("rear from empty queue")

    def size(self):
        return len(self.items)

    def clear(self):
            self.items = []

    def show(self):
        print("Full Queue:", self.items)

#Example usage:
queue = Queue()
# print("Front Element:", queue.get_front())
# print("Dequeued Element:", queue.dequeue())

queue.enqueue("Apple")
queue.enqueue("Banana")
queue.enqueue("Cherry")
print(queue.is_empty())

queue.show()
print("Queue Size:", queue.size())
print("Front Element:", queue.get_front())
print("Rear Element:", queue.get_rear())
print("Dequeued Element:", queue.dequeue())
queue.show()

queue.clear()
queue.show()
print(queue.is_empty())

print()

#REVERSE
str = 'Horse'
rev_str = Stack()

for x in str:
    rev_str.push(x)
print("String:", str)
print("Reversed word: ")
for x in range(0, len(str)):
    print(rev_str.pop(), end = "")