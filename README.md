# new_assignment
New Assignment from 21/05/2025

## Class_ex 

In Python, a class serves as a blueprint or a template for creating objects. It defines the structure and behavior that objects of that class will possess.

### Class:

    A class is a user-defined data type that encapsulates data (attributes or variables) and functions (methods) into a single unit.
    It is created using the class keyword.Attributes represent the properties or characteristics that objects of the class will have.
    Methods are functions defined within the class that operate on the object's data and define its behavior.


### Object:

    An object is a concrete instance of a class.


It is created from a class and holds actual values for the attributes defined in the class.
Each object created from a class is independent and maintains its own set of attribute values. 
Objects can access the attributes and call the methods defined in their class.


In Python, methods within a class can be categorized into three types based on their relationship with the class and its instances: 

### Instance Methods:

        These are the most common type of methods in a class.
        They operate on an instance (object) of the class and have access to instance-specific data (instance variables).
        They are defined with self as their first parameter, which refers to the instance itself.
        Instance methods can access and modify both instance attributes and class attributes. 

    class MyClass:
        def __init__(self, value):
            self.instance_value = value

        def instance_method(self):
            print(f"Instance method called. Instance value: {self.instance_value}")


### Class Methods:

    These methods are bound to the class itself, not to a specific instance.

They are defined using the @classmethod decorator.
Their first parameter is conventionally named cls, which refers to the class object itself.
Class methods can access and modify class-level attributes, but they cannot directly access instance-specific data unless an instance is passed to them.
They are often used for alternative constructors or for operations that involve the class as a whole.

    class MyClass:
        class_attribute = "Hello"

        @classmethod
        def class_method(cls):
            print(f"Class method called. Class attribute: {cls.class_attribute}")

### Static Methods:

    These methods do not depend on the class or instance state. 

They are defined using the @staticmethod decorator.
They do not implicitly receive self or cls as their first parameter.
Static methods are essentially regular functions that are logically grouped within a class for organizational purposes. They cannot access instance or class attributes directly.
They are typically used for utility functions that are related to the class but do not require access to its internal state.

    class MyClass:
        @staticmethod
        def static_method(message):
            print(f"Static method called: {message}") 



## Decorators 

    In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods without directly altering their source code. They are essentially higher-order functions that take another function as an argument and return a new function, typically with enhanced or modified functionality. 
How Decorators Work:

    Function as Argument: A decorator function takes the function it is decorating as an argument.
    Wrapper Function: Inside the decorator, a nested function (often called a "wrapper") is defined. This wrapper function encapsulates the original function and adds any desired additional logic (e.g., logging, timing, authentication).
    Return Wrapper: The decorator function returns this wrapper function.
    Syntactic Sugar: Python provides the @decorator_name syntax as a convenient way to apply decorators. Placing @decorator_name directly above a function definition is equivalent to my_function = decorator_name(my_function)

## Abstraction in python's OOPS concept

Abstraction in Python, a core principle of Object-Oriented Programming (OOP), 
involves hiding the complex implementation details of a system and exposing only the essential functionalities to the user. 
This means users interact with a simplified interface, knowing what a component does without needing to know how it does it.


    Key aspects of abstraction in Python:

    Focus on essential features:
            Abstraction emphasizes providing a high-level view, concentrating on the behavior and purpose of an object rather than its internal workings.

    Achieved through Abstract Base Classes (ABCs):
            Python uses the abc module and the ABC class to define abstract classes and methods. An abstract class cannot be instantiated directly and serves as a blueprint for other classes.
    
    Abstract methods:
            These are methods declared within an abstract class without an implementation. Subclasses inheriting from an abstract class are required to provide their own concrete implementations for these abstract methods. 
            This enforces a common interface across related classes.
    
    Simplifying complexity:
            Abstraction helps manage complexity by breaking down a system into smaller, more manageable components, each with a clearly defined interface.

    Enhancing maintainability and modularity:
            By separating interface from implementation, abstraction makes code more modular, easier to understand, and less prone to errors when changes are made to internal workings.

