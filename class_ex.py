class Employee:
    #Creating Employee class with instance methods , class methods , static method with object,class/static variables
    company_name = "company" #class/static variable
    company_mail = "company@company.com"

    def __init__(self,name,age,reg_no,salary): #constructor method
        """
        a constructor is a special method used to initialize the attributes of an object when a class is instantiated.
        It is automatically invoked whenever a new object of a class is created.

        The primary constructor in Python is the __init__ method.
        Key characteristics of the __init__ method:

        Automatic Invocation:
        It is automatically called by Python when an object of the class is created.
        Initialization:
        Its main purpose is to set the initial state of the object by assigning values to its attributes.
        self parameter:
        The first parameter of the __init__ method is always self, which refers to the instance of the class being created. This allows access to the object's attributes and methods.
        Optional Parameters:
        It can accept additional parameters to pass initial values to the object's attributes during creation.
        """
        self.name = name
        self.age = age
        self.reg_no = reg_no
        self.__salary = salary

    def show_details(self): #instance method
        """
        Purpose: These are the most common type of method and operate on a specific instance (object) of a class.
        They are used to access and modify the instance's data (attributes).
        First Argument: They implicitly receive the instance itself as their first argument, conventionally named self.
        Decorator: No special decorator is needed.
        """
        print(f"Employee details with name : {self.name} & Age : {self.age} & reg_number is : {self.reg_no}")


    @classmethod
    def class_method(cls): #class method
        """
        Purpose: These methods operate on the class itself rather than a specific instance.
        They are often used for factory methods (alternative constructors) or to interact with class-level data.
        First Argument: They implicitly receive the class itself as their first argument, conventionally named cls.
        Decorator: They are defined using the @classmethod decorator.
        """
        print(f"The Employee is working in company called : {cls.company_name}")

    @staticmethod
    def static_method(num1,num2): #static method
        """
        Purpose: These methods are essentially regular functions that are logically grouped within a class but do not operate on the instance or the class itself. They are typically used for utility functions that don't depend on any class or instance state.
        First Argument: They do not receive any implicit first argument (self or cls).
        Decorator: They are defined using the @staticmethod decorator.
        """
        return num1+num2

    #instance method
    def appraisal_hike(self,hike_percentage):
       return self.__salary * hike_percentage


Emp = Employee("Giri",25,912345,180000)
Emp.show_details()
Emp.class_method()
print(f"Static method return value - {Emp.static_method(5,6)}")
print(f"New Apprisal hike for employee is - {Emp.appraisal_hike(0.15)}")





