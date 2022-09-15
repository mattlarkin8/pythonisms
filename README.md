# **LAB - Class 42**

## **Project: Pythonisms**

### Author: Matthew Larkin

### Tests

Use `python linked_list_iterator.py` to run the main program and test the decorators.

Use `pytest` to run the tests and verify the functionality of all dunder methods.

### Lessons Learned

The different dunder methods usually have names that correspond to what they do. This helps when you need to find a specific method. For example, if you know you need to work with the length of something, you can start searching for length and easily find `__len__` is what you want.

Being able to use dunder methods to make custom data structures iterable or comparable is super cool and also very useful. So much of the code in this entire course could have been simplified if our linked lists were iterable. I'm going to start adding these dunder methods when I can so that I get this nice functionality in my data structures.

Decorators can continue to be wrapped or layered on top of each other to create some crazy effects. The decorators are resolved from the top down, so changing the order could drastically change your output depending on the operations performed.
