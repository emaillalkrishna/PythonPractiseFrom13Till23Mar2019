# # --------------------------------------------------Numbers------------------------------------------------------
# x = 1  # int
# y = 2.8  # float
# z = 1j  # complex
#
# print(type(x))
# print(type(y))
# print(type(z))
#
# print(id(x))
# print(id(y))
# print(id(z))

# # Python Casting
# # # Python  Integer Casting
# x = int(1)
# y = int(2.8)
# z = int("3")
#
# print(x)
# print(y)
# print(z)
#
# print(type(x))        # x will be 1             with type as <class 'int'>
# print(type(y))        # y will be 2             with type as <class 'int'>
# print(type(z))        # z will be 3             with type as <class 'int'>

# a = int("2.8")
# print(a)      # ValueError :
# it can constructs an integer number from a string literal (providing the string represents a whole number(integer)


# # # Python  Float Casting
# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
#
# print(x)
# print(y)
# print(z)
# print(w)
#
# print(type(x))        # x will be 1.0             with type as <class 'float'>
# print(type(y))        # y will be 2.8             with type as <class 'float'>
# print(type(z))        # z will be 3.0             with type as <class 'float'>
# print(type(w))        # w will be 4.2             with type as <class 'float'>


# # # Python String Casting
# x = str(2)
# y = str(3.0)
# z = str("QSpiders")
#
# print(x)
# print(y)
# print(z)
#
# print(type(x))        # x will be '2'         with type as <class 'str'>
# print(type(y))        # y will be '3.0'       with type as <class 'str'>
# print(type(z))        # z will be 'QSpiders'  with type as <class 'str'>


# # --------------------------------------------------String------------------------------------------------------
# # String
# a = "Hello, World"
# print(a)
# print(type(a))          # a will be 'Hello, World'     with type as <class 'str'>

# # Getting the characters of a string
# a = "Hello, World"
# print(a[0])
# print(a[-1])

# # Sub-string
# b = "Hello, World"
# print(b[2:5]) # Ans will be 'llo' ,Getting the characters from position 2 to till position 5(Value at 5 not included)


# # #  The len() method returns the length of a string:
# a = "Hello, World!"
# print(len(a))       # Ans is 13

# # # The lower() method returns the string in lower case:
# a = "Hello, World!"
# print(a.lower())

# # # The upper() method returns the string in upper case:
# a = "Hello, World!"
# print(a.upper())


# # # The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("H", "J"))    # returns 'Jello, World!'

# # # The split() method splits the string into substrings if it finds instances of the separator:
# a = "Hello, World!"
# print(a.split(","))             # returns ['Hello', ' World!']
# print(type(a.split(",")))       # where the type will be <class 'list'>

#
# # # # the count() method give the count of a specific item in a string
# a = "Hello, World!"
# print(a.count("l"))


