---
longform:
  format: single
  title: Constructor
---
A constructor in Python is a special method that is automatically called when an object of a class is created. The primary purpose of a constructor is to initialize the object's attributes.

In Python, the constructor method is defined using the `__init__` method. Here's how it works:

- The `__init__` method is automatically called when an instance of the class is created.
- It takes `self` as the first parameter, which refers to the instance being created.
- You can pass additional parameters to `__init__` to initialize the object's attributes.

```
class Dog:
    def __init__(self, name, age):
        # These are instance attributes
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")

# Calling a method
print(my_dog.bark())

```

### Output

```
My dog's name is Buddy and he is 3 years old.
Buddy says woof!
```