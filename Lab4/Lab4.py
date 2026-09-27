###Q1. Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

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

    def show(self):
        print("Full Stack:", self.items)

#Example usage:
stack = Stack()

stack.push("Horse")
stack.push("Dog")
stack.push("Zebra")

stack.show()
print("Stack Size:", stack.size())
print("Top Element:", stack.peek())
print("Popped Element:", stack.pop())
stack.show()

###Q1. Queue Implementation
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)

    def show(self):
        print("Full Queue:", self.items)

#Example usage:
queue = Queue()

queue.enqueue("Apple")
queue.enqueue("Banana")
queue.enqueue("Cherry")

queue.show()
print("Queue Size:", queue.size())
print("Front Element:", queue.peek())
print("Dequeued Element:", queue.dequeue())
queue.show()
