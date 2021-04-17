# python-OOP
python OOP samples


## Overview of OOP Terminology

**Class variable**
A variable that is shared by **all instances** of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

**Instance variable**:
 A variable that is defined inside a method and belongs **only to the current instance** of a class.

**Instance Method**
-Instance methods can freely access attributes and other methods on the same object. 
-Instance methods can modify an **object’s state** and **class state**.

**Class Method**
-class methods take a `cls` parameter that points to the class. 
-Because the class method only has access to this `cls` argument, it **can’t modify object instance state**.  
-class methods can **modify class** state that applies across all instances of the class.

**Static Method**
Static method can neither modify **object state** nor **class state**. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
