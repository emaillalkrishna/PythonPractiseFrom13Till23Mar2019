# # # ----------------------------------------------------------------------------------------------
# # # --------------------------Case1 : Positional arguments------------------------------
# # # ----------------------------------------------------------------------------------------------
# def sum_of_numbers(x, y):
#     z = x + y
#     print("Addition of 2 numbers is ", z)
#
#
# sum_of_numbers(2, 3)            # Ans : Addition of 2 numbers is  5


# # # ----------------------------------------------------------------------------------------------
# # # --------------------------Case2 : Default arguments------------------------------
# # # ----------------------------------------------------------------------------------------------
#
# def my_function(a, b, c=10):
#     print(a, b, c)
#
#
# my_function(1, 2, 3)        # Ans: 1 2 3


# def my_function(a, b=10):
#     print(a, b)
#
#
# my_function(1, 2)        # Ans: 1 2

#
# def my_function(a=10, b):
#     print(a, b)
#
#
# my_function(1, 2)           #ans: SyntaxError: non-default argument follows default argument

# def sum_of_numbers(a, b, c=10, d=20):
#     print(a, b, c, d)
#
#
# sum_of_numbers(1, 2, 3, 4)                        # Ans : 1 2 3 4


# def sum_of_numbers(a, b, c=10, d=20):
#     print(a, b, c, d)
#
#
# sum_of_numbers(1, 2, 3)                           # Ans : 1 2 3 20


# def sum_of_numbers(a, b, c=10, d=20):
#     print(a, b, c, d)
#
#
# sum_of_numbers(1, 2)                                # Ans": 1 2 10 20
#
#
# def sum_of_numbers(a, b, c=10, d=20):
#     print(a, b, c, d)
#
#
# sum_of_numbers(1)                          # TypeError: sum_of_numbers() missing 1 required positional argument: 'b'


# def function_name(a=10, b):
#     print(a, b)
#
#
# function_name(1, 2)                         # Ans: SyntaxError: non-default argument follows default argument


# # # ----------------------------------------------------------------------------------------------
# # # ---------------------------Case3 : Positional arguments with Keyword arguments------------------------------
# # # ----------------------------------------------------------------------------------------------


# def roi(p, t, r):
#     roi = (p * t * r) / 100
#     print(p, t, r)
#
#
# roi(1000, 12, 10)           # Ans: 1000 12 10

#
# def roi(p, t, r):
#     roi = (p * t * r) / 100
#     print(p, t, r)
#     print("Balance is ", roi)
#
#
# roi(2000, 12, 10)           # Ans: 2000 12 10 ----> Balance is  2400.0
#
#
# def roi(p, t, r):
#     roi = (p * t * r) / 100
#     print(p, t, r)
#     print("Balance is ", roi)
#
#
# roi(1000, t=12, r=10)           # Ans: 1000 12 10 ----> Balance is  1200.0
#
#
# def roi(p, t, r):
#     roi = (p * t * r) / 100
#     print(p, t, r)
#     print("Balance is ", roi)
#
#
# roi(1000, r=10, t=12)           # Ans: 1000 12 10 ----> Balance is  1200.0
#
#
# def roi(p, t, r):
#     roi = (p * t * r) / 100
#     print(p, t, r)
#     print("Balance is ", roi)
#
#
# roi(t=12, r=10, 1000)              # Ans: SyntaxError: positional argument follows keyword argument
# # Reason  why the error came →
# #  Note :Positional argument should not be followed by the keyword argument
# #  Positional argument →  1000
# #  keyword argument → t=12 and r=10
#
#

# # # ----------------------------------------------------------------------------------------------
# # # ---------------------------Case 4. Default arguments with Keyword arguments ------------------------------------
# # # ----------------------------------------------------------------------------------------------

# def function_name(a, b, c=20, d=30):
#     print(a, b, c, d)
#
#
# function_name(10, 20, c=30, d=40)           # Ans: 10 20 30 40


# def function_name(a, b, c=20, d=30):
#     print(a, b, c, d)
#
#
# function_name(10, 20, c=30)                     # Ans: 10 20 30 30


# def function_name(a, b, c=20, d=30):
#     print(a, b, c, d)
#
#
# function_name(20, c=30, d=40, 10)      # Ans: SyntaxError: positional argument follows keyword argument

# def function_name(a, b, c=30):
#     print(a, b, c)
#
#
# function_name(1, 2, 3)          # Ans : 1 2 3
# function_name(1, 2, c=33)       # Ans : 1 2 33
# # #  ----------------------------------------------------------------------------------------------
# # # ---------------------------Case 5. Variable arguments-------------------------------------
# # # ----------------------------------------------------------------------------------------------


# def sum_of_n_num(*x):
#     print(x)
#     s = (0)
#     for i in x:
#         s = s + i
#     print(s)
#
#
# sum_of_n_num(2, 3)  # Ans:x is tuple (2, 3)-->When we print the Value of s then we get s=5

# def sum_of_n_num(*x):
#     print(x)
#     s = (0)
#     for i in x:
#         s = s + i
#     print(s)
#
#
# sum_of_n_num(2, 3, 4)  # Ans:x is tuple(2, 3, 4)-->When we print the Value of s then we get s=9
#
#
# def sum_of_n_num(*x):
#     print(x)
#     s = (0)
#     for i in x:
#         s = s + i
#     print(s)
#
#
# sum_of_n_num()      #  Ans:x is tuple()-->When we print the Value of s then we get s=0


# # # ----------------------------------------------------------------------------------------------
# # # ---------------------------Case 6. Variable arguments with a default argument------------------------------------
# # # ----------------------------------------------------------------------------------------------

#
# def sum_of_n_num(*x):
#     print(x)
#     print(type(x))
#
#
# sum_of_n_num(1, 2, 3, 4, 5)  # Ans: when we print x=(1, 2, 3, 4, 5) and type of x is = <class 'tuple'>


# def f_name(a, b=100, *x):
#     print(a, b)
#     print(x)
#     for i in x:
#         print(i)
#
#
# f_name(1, 2, 3, 4) # Ans:When we print the value of a&b then we get 1,2. When we print x value then we get tuple(3, 4)


# Positional argument with Variable argument
# def my_function(a=100, *x):
#     print(x)
#     print(a)
#
#
# my_function(1, 2, 3, 4, 5)  # Ans : x = (2, 3, 4, 5) and a= 1

# # # ----------------------------------------------------------------------------------------------------------
# # # ----------------------------------------------------------------------------------------------------------
# # # ----------------------------------------------------------------------------------------------------------

# # # -----------------------------------Function return types-----------------------------------------------
# # -------------------------------Case 1: Single value return type --------------------------------------
# def my_function(x, y):
#     z = x + y
#
#
# my_var = my_function(2, 3)
# print(my_var)            # Ans: None

# def my_function(x, y):
#     z = x + y
#     return z
#
#
# my_var = my_function(2, 3)
# print(my_var)       # Ans: After adding the two values, it returns the value = 5
#
#
# def my_function(x, y):
#     z = x + y
#     return
#
#
# my_var = my_function(2, 3)
# print(my_var)      # Ans: We are using return statement, but not mentioned the return variable name(identifier name)

#
# def my_function(x, y):
#     z = x + y
#     print("Before return statement")
#     return
#     print("After return statement")
#
#
# my_var = my_function(2, 3)
# print(my_var)
#
# def my_function(x, y):
#     z = x + y
#     print("Before return statement")
#     return z
#     print("After return statement")
#
#
# my_var = my_function(2, 3)
# print(my_var)

# # -----------------------------Case 2: Multi value return type ------------------------------------
# def my_function(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# my_var = my_function(2, 3)
# print(my_var)           # Ans: 3

# # -----------------------------Case 3: Collections/Arrays as a return type  ------------------------------------

# def my_function():
#     return [1, 2, 3, 4]
#
#
# my_var = my_function()
# print(my_var)


# def my_function():
#     return (1, 2, 3, 4)
#
#
# my_var = my_function()
# print(my_var)


# def my_function():
#     return {1, 2, 3, 4}
#
#
# my_var = my_function()
# print(my_var)


# def my_function():
#     return {"one": 1, "two": 2, "three": 3, "four": 4}
#
#
# my_var = my_function()
# print(my_var)


# -------------------------------------------------------------------------------------

# # Q. Write a python program to add and Subscribe and multiply the given values and print the result in list format.
# def my_function(x, y):
#     return [x + y, x - y, x * y]
#
#
# my_var = my_function(2, 3)
# print(my_var)               # Ans: [5, -1, 6]

# # Q. Write a python program to perform addition and subtraction operation
# # ------  and return the values in the form of set and dictionary

# # # ------------------------------------------------------------------------------------------------------
# # # ----------------------------------Global Variable and Local variable--------------------------------------
# # # ------------------------------------------------------------------------------------------------------

# x = 10                      # global variable
#
#
# def my_function1():
#     x = 20                  # local variable, lifespan of local variable will be till the end of function execution
#     print(x)
#
#
# def my_function2():
#     x = 30                  # local variable, lifespan of local variable will be till the end of function execution
#     print(x)
#
#
# my_function1()              # 20
# my_function2()              # 30
# print(x)                    # 10

# # # Doubt: Here in this program we have introduced the keyword global.
# # # I am not able to understand what difference in brought to the Program
# # # Or did i wrote something wrong in this program

# x = 10                       # global variable
#
#
# def my_function():
#     global x                # Now we convert this to a global variable by using the keyword global
#     x = 20
#     print(x)
#
#
# my_function()               # Ans : 20
# print(x)                    # Ans : 10


# # # --------------------------------------- Documentation String -----------------------------------------
# # # Double underscore doc is used to access the method or class description
# # #
# # # The description should be inside a method.
# # # And also it should be enclosed within triple double quotes or triple single quotes.


# def my_function(x, y):
#     '''This method performs addition operation'''
#     z = x + y
#     print(z)
#
#
# my_function(2, 3)
# print(my_function.__doc__)


# # # --------------------------------------- String -----------------------------------------
# my_string1 = "QSpiders"
# print(type(my_string1))         # Ans: <class 'str'>
#
# my_string2 = 'btm'
# print(type(my_string2))         # Ans: <class 'str'>
#
# my_string3 = '''bangalore'''
# print(type(my_string3))         # Ans: <class 'str'>
#
# my_string4 = """python"""
# print(type(my_string4))         # Ans: <class 'str'>


# # Accessing the string elements using the index

# my_string = "QSpiders python  BTM"
# print(my_string.startswith('QSpider'))      # Ans : True
#
# my_string = "QSpiders python  BTM"
# print(my_string.startswith('python'))       # Ans: False
# print(my_string.startswith('python', 9))    # Ans : True


# # -------------------Syntax	: Startswith (String Value, Start Value, End Value)-----------------------------------

# my_string = "QSpiders python BTM"
# print(my_string.startswith(('QSpiders', 'python')))  # Ans: True
# print(my_string.startswith(('Selenium', 'python')))  # Ans: False
# print(my_string.startswith(('QSpiders', 'Selenium')))  # Ans: True
#
# print(my_string.startswith(('QSpiders', 'python'), 9))  # Ans: True
# print(my_string.startswith(('QSpiders', 'python'), 9, 20))  # Ans: True
# print(my_string.startswith(('QSpiders', 'python'), 19, 20))  # Ans: False
# print(my_string.startswith(('QSpiders', 'python'), 0, 20))  # Ans: True
#
# print(my_string.startswith(('Selenium', 'python'), 9))  # Ans: True

# # -------------------Syntax	: Endswith(Substring, Start Index , End Index)-----------------------------------
#
# my_string = "QSpiders Python BTM"
# print(my_string.endswith("BTM"))            # Ans: True
# print(my_string.endswith("Python"))         # Ans: False
# print(my_string.endswith("QSpiders"))       # Ans: False

#
# my_string = "QSpiders Python BTM"
# print(my_string.endswith("BTM"))          # Ans: True
# print(my_string.endswith("BTM", 2))       # Ans: True
# print(my_string.endswith("BTM", 16))      # Ans: True
# print(my_string.endswith("BTM", 17))      # Ans: False
#
#
# my_string = "QSpiders Python BTM"
# print(my_string.endswith("BTM"))            # Ans: True
# print(my_string.endswith("BTM", 2, 18))     # Ans: False
# print(my_string.endswith("BTM", 2, 19))     # Ans: True
# print(my_string.endswith("BTM", 16, 18))    # Ans: False
# print(my_string.endswith("BTM", 16, 19))    # Ans: True
# print(my_string.endswith("BTM", 17, 18))    # Ans: False
# print(my_string.endswith("BTM", 17, 19))    # Ans: False


# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# class Human:
#     def __init__(self):
#         self.eye = 2
#         self.name = 'Lal'
#         print(self.eye)
#         print(self.name)
#
#
# test_object_human1 = Human()            # Ans : 2 and Lal
# test_object_human2 = Human()            # Ans : 2 and Lal


# class Mobile:
#     def __init__(self):
#         self.name = 'Nokia'
#         self.camera = "15MP"
#         print(self.name)
#         print(self.camera)
#
#
# my_test_object_mobile1 = Mobile()          # Ans : Nokia and 15MP
# my_test_object_mobile2 = Mobile()          # Ans : Nokia and 15MP


# class House:
#     def __init__(self):
#         self.hall = 1
#         self.color = 'white'
#         print(self.hall)
#         print(self.color)
#
#
# my_test_object_house1 = House()             # Ans : 1 and White
# my_test_object_house2 = House()             # Ans : 1 and White

# class Human:
#     def __init__(self, manushyantePeru):
#         self.eye = 2
#         self.name = manushyantePeru
#         print(self.eye)
#         print(self.name)
#
#
# h1 = Human('lal')                               # Ans:  2 and Lal
# h2 = Human('kevin')                             # Ans:  2 and Kevin

# class Human:
#     eye = 2
#
#     def __init__(self, manushyantePeru):
#         self.name = manushyantePeru
#         print(Human.eye)
#         print(self.name)
#
#
# h1 = Human('lal')                               # Ans: 2 and Lal
# h2 = Human('kevin')                             # Ans: 2 and Kevin
#