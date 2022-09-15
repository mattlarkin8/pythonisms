from functools import wraps
import time

class LinkedList:
    """
    Used to create a singly linked list. Has methods to create a new node at the beginning of the list, search
    for a value in the list, and return a string that represents all items in the list.
    """

    def __init__(self, values=None):
        self.length = 0
        self.head = None
        if values:
            for value in reversed(values):
                self.insert(value)

    def __str__(self):
        out = ""
        current = self.head
        while current:
            out += f"{{ {current.value} }} -> "
            current = current.next

        return out + "None"

    def __iter__(self):
        def value_potato():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_potato()

    def __len__(self):
        return self.length

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError

    def insert(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            self.length += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)
            self.length += 1

    def insert_before(self, idx, new):
        if self.head is None:
            raise TargetError

        current = self.head
        if current.value == idx:
            new_node = Node(new)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return f"Successfully created {new}!"

        while current and current.next is not None:
            if current.next.value == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                return f"Successfully created {new}!"
            current = current.next
        raise TargetError

    def insert_after(self, idx, new):
        if self.head is None:
            raise TargetError

        current = self.head
        while current:
            if current.value == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                return f"Successfully created {new}!"
            current = current.next
        raise TargetError

    def includes(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError

        length = self.get_length()

        if k >= length:
            raise TargetError

        target_idx = (length - 1) - k
        current_idx = 0
        current = self.head
        while current:
            if current_idx == target_idx:
                return current.value
            current_idx += 1
            current = current.next

class Node:
    def __init__(self, val, next_ = None):
        self.value = val
        self.next = next_

class TargetError(Exception):
    pass

# Decorators
def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return orig_val.upper()
    return wrapper

def slow(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper()

def timer(func): # from https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} took {total_time} seconds")
        return result
    return wrapper()

# @slow
@announce
def say(txt):
    return txt

print(say("This is a test of the announcement system."))

# @timer
def calculate(num):
    total = sum((x for x in range(0, num**2)))
    return total

calculate(10)
calculate(100)
calculate(1000)