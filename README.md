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

    
    on the above example , if we try to change the class variable(class_attribute to "Yallo" from "Hello")
    by using classname.class_variable(MyClass.class_attribute) or instance.class_variable .
    then every time when we create new object , the new object will have the latest value on the class variable(Yallo).


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

Abstraction is at design level, here we try to identify which methods/attributes that we wanted to hide it
from the user & which one to show it user. so after idetifying the implementation will be done through some of 
the access specifiers like - public , private & protected (Encapsulation features).
    
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



## Webscrape : BeautifulSoup 

Web scraping is the process of automatically extracting data from websites. 
It involves using bots, also known as web scrapers, to retrieve data from websites, often by parsing the underlying HTML code. 
This technique is used for various purposes, including data mining, price monitoring, and content aggregation


Key Python Libraries for Web Scraping:

    Requests: For making HTTP requests.
    BeautifulSoup: For parsing HTML/XML and navigating the parse tree.
    lxml: A fast and powerful XML and HTML parser, often used with XPath.
    Selenium/Playwright: For automating browser interactions and scraping dynamic content.
    Scrapy: A comprehensive web crawling framework for larger-scale scraping projects.

## Webscrape : Selenium

To use Selenium with Python, you'll primarily need to install the selenium Python package using pip and then install a WebDriver for your preferred browser. 
Selenium allows you to automate browser interactions for testing web applications.

Install the below things before proceeding further :
    
    pip install requests
    pip install selenium
    sudo apt-get install chromium-chromedriver 

## [shallow_deep_=_.py](shallow_deep_%3D_.py)

'=' Operator operation will creates new variable but pointing to same memory address of the original
variable was pointing , hence the any changes made on new will also affect the original variable's content.


#### **shallow copy** 

    Shallow copy creates a new object & it doesn't create copies of the object contained in the
    original ,instead of it creates/insert reference to the same object that original object contains.

on normal list-  

    Changes were made in shallow copy object wont get reflect on the original object , on single/normal
    list the shallow copy behaves exactly same as deep copy.

on nested list-  

    Changes were made in shallow copy object gets reflect on the original object.

#### **deep copy**

    Deep copy creates completely new & independent copy of the original object.
    changes were made to the deep copy object including nested objects will not affect the original object.

## [ScrapeTable.py](ScrapeTable.py)

    With help of selenium & python , scraped the data from web table in an easy way. 