# # # Creating a class with a method and creating object from that blue print class
#
#
# class Person:
#     def __init__(self, fname, lname):  # Creating receiving centers for accepting the properties of the object
#         self.first_name = fname
#         self.last_name = lname
#
#     def my_method(self):
#         print("My name is " + self.first_name + " " + self.last_name)  # Creating method of the class
#
#
# p1 = Person("Kevin", "Jose")  # Providing properties of the object
# p1.my_method()


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


# class Human:
#     def __init__(self):
#         self.eye = 2
#         self.scientificname = 'Homosapien'
#         print(self.eye)
#         print(self.scientificname)
#
#
# test_object_man = Human()               # Ans : 2 and Homosapien
# test_object_women = Human()             # Ans : 2 and Homosapien

# ------------------------------------------------------------------------------------------------------------

# class Human:
#     def __init__(self, Person_Name):
#         self.eye = "Number of eyes:2"
#         self.scientificname = 'Homosapien'
#         self.name = Person_Name
#         print(self.eye)
#         print(self.scientificname)
#         print(self.name)
#
#
# test_object_man = Human('Jayaram')          # Ans:  Number of eyes:2  , Homosapien , Jayaram
# test_object_woman = Human('Parvathi')       # Ans:  Number of eyes:2  , Homosapien , Parvathi

# ------------------------------------------------------------------------------------------------------------

# class Human:
#     eye = "Number of eyes:2"
#     scientific_name = "Homosapien"
#
#     def __init__(self, Person_Name):
#         self.name = Person_Name
#         print(self.eye)
#         print(self.scientific_name)
#         print(self.name)
#
#
# test_object_man = Human('Jayaram')  # Ans:  Number of eyes:2  , Homosapien , Jayaram
# test_object_woman = Human('Parvathi')  # Ans:  Number of eyes:2  , Homosapien , Parvathi

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------Static variable or Class level variable--------------------------------------

# class Human:
#     eye = "Number of eyes:2"
#     scientific_name = "Homosapien"
#
#     def __init__(self, Person_Name):
#         self.name = Person_Name
#         print(Human.eye)
#         print(Human.scientific_name)
#         print(self.name)
#
#
# test_object_man = Human('Jayaram')          # Ans:  Number of eyes:2  , Homosapien , Jayaram
# test_object_woman = Human('Parvathi')       # Ans:  Number of eyes:2  , Homosapien , Parvathi

# ------------------------------------------------------------------------------------------------------------

# class Human:
#     eye = "Number of eyes:2"
#     scientific_name = "Homosapien"
#
#     def __init__(self, Person_Name):
#         self.name = Person_Name
#         print(Human.eye)
#         print(Human.scientific_name)
#         print(Human.name)
#
#
# test_object_man = Human('Jayaram')              # Ans: AttributeError: type object 'Human' has no attribute 'name'
# test_object_woman = Human('Parvathi')           # Ans: AttributeError: type object 'Human' has no attribute 'name'

# ------------------------------------------------------------------------------------------------------------


# # # -----------------------------------------------------------------------------------------------------------
# # # -------------------------------------       Instance Method     ------------------------------------------
# # # Instance Method. #For instance, method first argument should be self. #Instance method should be called explicitly

# class Human:
#     def my_method1(self):
#         print('inside instance method')
#
#     def __init__(self):
#         print('inside constructor')
#
#
# my_object = Human()             # Ans: inside constructor
# my_object.my_method1()          # Ans: inside instance method


# # # -----------------------------------------------------------------------------------------------------------
# # # -----------------------------------------------------------------------------------------------------------

# # Case1. Declaring variable in an instance method
# class Human:
#     def my_method(self):
#         self.name = 'Homosapien'
#         print(self.name)
#
#
# h1 = Human()
# h1.my_method()                      # Ans: Homosapien

# # Case 2: Declare and initialize a variable inside a constructor
# class Human:
#     def __init__(self):
#         self.name = 'Homosapien'
#         print(self.name)
#
#
# my_object = Human()                         # Ans: Homosapien
#
# # Case 3: Declare and initialize the instance variable in a constructor and access them in an instance method

# class Human:
#     def __init__(self):
#         self.name = 'Homosapien'
#
#     def my_method(self):
#         print(self.name)
#
#
# my_object = Human()
# my_object.my_method()                           # Ans: Homosapien
#
# # Case 4: Declare and initialize the instance variable in a instance method and access them in constructor

# class Human:
#     def __init__(self):
#         print(self.name)
#
#     def my_method(self):
#         self.name = 'Homosapien'
#
#
# my_object = Human()                             # Ans: AttributeError: 'Human' object has no attribute 'name'
# my_object.my_method()


# # Case 5: Declare and initialize instance variable inside one instance methods
# #         and access them in an another instance method
# class Human:
#     def my_method1(self):
#         self.name = 'Homosapien'
#
#     def my_method2(self):
#         print(self.name)
#
#
# my_object_man = Human()
# my_object_man.my_method1()
# my_object_man.my_method2()                  # Ans: Homosapien


# class Human:
#     def my_method1(self):
#         self.name = 'Homosapien'
#
#     def my_method2(self):
#         print(self.name)
#
#
# my_object_man = Human()
# my_object_man.my_method2()              # Ans: AttributeError: 'Human' object has no attribute 'name'
# my_object_man.my_method1()


# # # -----------------------------------------------------------------------------------------------------------
# # # -----------Declaring and initializing a static variable and accessing them in a different level-------------
# # # -----------------------------------------------------------------------------------------------------------

# class Human:
#     eye = 2                                         # This is a static variable
#
#     def __init__(self):                             # This is a constructor
#         print("Constructor: ", Human.eye)
#
#     def my_method1(self):                           # This is a Method
#         print("my_method1: ", Human.eye)
#
#     @classmethod                                    # This is a class method decorator
#     def my_method2(cls):
#         print("class method: ", Human.eye)
#
#     @staticmethod                                   # This is a static method decorator
#     def my_method3():
#         print("static method: ", Human.eye)
#
#
# my_object_man = Human()                             # Ans: Constructor      :  2
# my_object_man.my_method1()                          # Ans: my_method1       :  2
# my_object_man.my_method2()                          # Ans: class method     :  2
# my_object_man.my_method3()                          # Ans: static method    :  2


# # # With the static variable, Access them in an instance method and outside the class
# class Human:
#
#     def __init__(self):
#         Human.eye = 2
#         print("Inside 'constructor': ", Human.eye)
#
#     def my_method(self):
#         print("Inside 'my_method': ", Human.eye)
#
#
# my_object_man = Human()                         # Ans: Inside 'constructor' : 2
# my_object_man.my_method()                       # Ans: Inside 'my_method'   : 2
# print("Outside 'class':", Human.eye)            # Ans: Outside 'class'      : 2


# # # ---------------------------------------------------------------------------------------------------------
# # # ---------------------------------------------------------------------------------------------------------


# class Human:
#
#     def __init__(self):
#         Human.eye = 2
#         print(Human.eye)
#
#     def m1(self):
#         print("m1: ", Human.eye)
#
#     @classmethod
#     def m2(cls):
#         print("class: ", Human.eye)
#
#     @staticmethod
#     def m3():
#         print("static: ", Human.eye)
#
#
# h = Human()
# h.m1()
# h.m2()
# h.m3()


# class Human:
#
#     def __init__(self):
#         print(Human.eye)
#
#     def m1(self):
#         Human.eye = 2
#         print("m1: ", Human.eye)
#
#     @classmethod
#     def m2(cls):
#         print("class: ", Human.eye)
#
#     @staticmethod
#     def m3():
#         print("static: ", Human.eye)
#
#
# h = Human()
# h.m1()
# h.m2()
# h.m3()


# class Human:
#
#     def __init__(self):
#         print(Human.eye)
#
#     def m1(self):
#         print("m1: ", Human.eye)
#
#     @classmethod
#     def m2(cls):
#         Human.eye = 2
#         print("class: ", Human.eye)
#
#     @staticmethod
#     def m3():
#         print("static: ", Human.eye)
#
#
# h = Human()
# h.m1()
# h.m2()
# h.m3()


class Human:

    def __init__(self):
        print(Human.eye)

    def m1(self):
        print("m1: ", Human.eye)

    @classmethod
    def m2(cls):
        print("class: ", Human.eye)

    @staticmethod
    def m3():
        Human.eye = 2
        print("static: ", Human.eye)


h = Human()
h.m1()
h.m2()
h.m3()
