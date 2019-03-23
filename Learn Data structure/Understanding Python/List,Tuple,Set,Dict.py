# # # # List and List Constructor
# # # List
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# # # List Constructor
# thislist = list(("apple", "banana", "cherry"))
# print(thislist)

# # # # -------------------------------- iterating through a list using the for loop ---------------------
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)


# # # ------------------------------------Adding an item to an existing list---------------------------------
# # 1. To add an item to the end of the list, use the append() method
# thislist = list(("apple", "banana", "cherry"))
# thislist.append("orange")
# print(thislist)               # Ans: ['apple', 'banana', 'cherry', 'orange']


# # 2. To add an item at the specified index, use the insert() method
# thislist = list(("apple", "banana", "cherry"))
# thislist.insert(1, "mango")
# print(thislist)                 # Ans: ['apple', 'mango', 'banana', 'cherry']

# # # ---------------------------Removing an item from a list---------------------------------------------
# # 1. The remove() method removes the specified item
# thislist = list(("apple", "banana", "cherry"))
# thislist.remove("banana")
# print(thislist)                     # Ans: ['apple', 'cherry']

# thislist = list(("apple", "banana", "cherry"))
# thislist.remove("banana","cherry")
# print(thislist)                     # Ans: TypeError: remove() takes exactly one argument (2 given)

# # 2. The pop() method removes the specified index, (or the last item if index is not specified)

# # pop() method remove an item in the specified index when the index is provided
# thislist = list(("apple", "banana", "cherry"))
# thislist.pop(0)
# print(thislist)                     # Ans: ['banana', 'cherry']

# # pop() method removing the last item when the index is not mentioned
# thislist = list(("apple", "banana", "cherry"))
# thislist.pop()
# print(thislist)                      # Ans: ['apple', 'banana']

# thislist = list(("apple", "banana", "cherry"))
# thislist.pop(1,2)
# print(thislist)                      # Ans: TypeError: pop() takes at most 1 argument (2 given)

# # The clear() method empties the list:
#
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)                         # Ans: []
#
# thislist = ["apple", "banana", "cherry"]
# thislist.clear(1)
# print(thislist)                             # Ans: TypeError: clear() takes no arguments (1 given)

# # # Removing an item using del keyword →
# # The del keyword removes the specified index when the index is provided
# thislist = list(("apple", "banana", "cherry"))
# del thislist[0]
# print(thislist)                         # ['banana', 'cherry']

# # The del keyword delete the entire list when the index is not provided
# thislist = list(("apple", "banana", "cherry"))
# del thislist
# print(thislist)                         # Ans: NameError: name 'thislist' is not defined


# # # --------------------------Changing the value of an existing item present in a list-------------
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "mango"
# print(thislist)


# # # --------------------------Check if Item Exists-------------

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")      # Ans: Yes, 'apple' is in the fruits list

# # # -----------------------Reversing the list items ------------------------
# thislist = ["apple", "banana", "cherry"]
# thislist.reverse()
# print(thislist)             # Ans: ['cherry', 'banana', 'apple']


# # # -----------------------------Sorting the list items -----------------------
# thislist = ["apple", "cherry" , "banana"]
# thislist.sort()
# print(thislist)             # Ans: ['apple', 'banana', 'cherry']


# thislist = [1, 3, 2, 5, 4]
# thislist.sort(reverse=True)
# print(thislist)             # Ans: [5, 4, 3, 2, 1]
#
# thatlist = [1, 3, 2, 5, 4]
# thatlist.sort(reverse=False)
# print(thatlist)             # Ans: [1, 2, 3, 4, 5]


# # # --------------------------Finding the Length of the list using the len keyword -------------
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))  # Ans : 3


# # # ------------------------------------  Max and Min   --------------------------------------------------
# thislist = [1, 2, 3, 4, 5, 6, 1, 2, 3]
#
# print(max(thislist))  # Ans: 6
# print(min(thislist))  # Ans: 1


# # # ------------------------------------  Multiplication   --------------------------------------------------
# thislist = ["apple", "banana", "cherry"]
# thatlist = [1, 2, 3]
# print(thislist * 2)             # Ans: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
# print(thatlist * 3)             # Ans: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# thislist = [1, 2, 3]
# thatlist = [4, 5, 6]
# print(thislist * thatlist)      # Ans: TypeError: can't multiply sequence by non-int of type 'list'
#
# thislist = ["apple", "banana", "cherry"]
# thatlist = ["mango", "thenga", "chakka"]
# print(thislist * thatlist)      # Ans: TypeError: can't multiply sequence by non-int of type 'list'

# # # ------------------------------------  Concatenation of a list   ------------------------------------------------
# thislist = [1, 2, 3]
# thatlist = [4, 5, 6]
# biglist = thislist + thatlist
# print(biglist)                                # Ans: [1, 2, 3, 4, 5, 6]
#
# thislist = ["apple", "banana", "cherry"]
# thatlist = ["mango", "thenga", "chakka"]
# biglist = thislist + thatlist
# print(biglist)                                # Ans: ['apple', 'banana', 'cherry', 'mango', 'thenga', 'chakka']

# # #  ------------------------------------extend function ----------------------------------------------------
# thislist = ["apple", "banana", "cherry"]
# thatlist = ["mango", "thenga", "chakka"]
# thislist.extend(thatlist)
# print(thislist)                               # Ans: ['apple', 'banana', 'cherry', 'mango', 'thenga', 'chakka']


# # # ------------------------------------  Nested list   ------------------------------------------------
# thislist = [1, "Kevin", 10, ["apple", "banana"], 20]
# print(thislist[0])          # Ans: 1
# print(thislist[1])          # Ans: Kevin
# print(thislist[2])          # Ans: 108
# print(thislist[3])          # Ans: ['apple', 'banana']
# print(thislist[3][0])       # Ans: apple
# print(thislist[3][1])       # Ans: banana
# print(thislist[4])          # Ans: 20

# # # Question:  Get the result as shown below
# # # [1]
# # # [1, 2]
# # # [1, 2, 3]
# # # [1, 2, 3, 4]
# # # [1, 2, 3, 4, 5]

# # # Script
# l1 = []
# l2 = [1, 2, 3, 4, 5]
# for var in l2:
#     if var not in l1:
#         l1.append(var)
#         print(l1)

# l1 = []
# l2 = [1, 2, 3, 4, 5]
# for var in l2:
#     if var not in l1:
#         l1.append(var)
#     print(l1)

# l1 = []
# l2 = [1, 2, 3, 4, 5]
# for var in l2:
#     if var not in l1:
#         l1.append(var)
# print(l1)

# # # help(list)

# 20 Mar 2019 i am able to write and explain all these logic in less than 20 minutes.


# # # -----------------------------------------------------------------------------------------------------------------
# # # --------------------------------------------------Tuple---------------------------------------------------------
# # # -----------------------------------------------------------------------------------------------------------------

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)        # ('apple', 'banana', 'cherry')

# # #-----------------------------------------------Tuple Construction---------------------------------------
# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)


# # #--------------------------------------Adding an item to a tuple---------------------------------------
# # Not Applicable


# # #------------------------------------- Removing an item to a tuple---------------------------------------
# thistuple = ("apple", "banana", "cherry")
# del thistuple[0]
# print(thistuple)   # # Not Applicable         # Ans: TypeError: 'tuple' object doesn't support item deletion


# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)                    # Ans: NameError: name 'thistuple' is not defined

# # #-------------------------------------Changing the value of an existing item of a tuple--------------------------
# # Not Applicable


#
# # -------------------------------------Access Tuple Items-----------------------------------------------
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])                 # Ans: banana


# # # --------------------------- Checking the existence of an item -----------------------------
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#     print("Yes, 'apple' is in the fruits tuple")


# # # --------------------------- Iteration / Looping through the items of a tuple--------------------
# thistuple = ("apple", "banana", "cherry")
# for i in thistuple:
#     print(i)

# # # ---------------------------------Concatenation---------------------------------
# thistuple = ("apple", "banana", "cherry")
# thattuple = ("manga", "thenga", "chakka")
# bigtuple = thistuple+thattuple
# print(bigtuple)                 # ('apple', 'banana', 'cherry', 'manga', 'thenga', 'chakka')

#
# thistuple = (1, 2, 3)
# thattuple = (4,5,6)
# bigtuple = thistuple+thattuple
# print(bigtuple)                 # Ans: (1, 2, 3, 4, 5, 6)

# # # -----------------------------------Finding the length of a tuple ------------------------------
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))               # Ans: 3

# # # -----------------------------------Sorting the tuple values ------------------------------
# # Not Applicable

# # # ----------------------------------- Reversing the tuple ------------------------------
# # Not Applicable

# # # --------------------------------Finding the Max and Min value in a tuple------------------------------
# thistuple = (1,2,3,4,5)
# print(max(thistuple))               # Ans: 5
# print(min(thistuple))               # Ans: 1


# # # -------------------------------- Nested Tuple -------------------------
# thistuple = (1, 2, ("apple", "banana", "cherry"), 3, 4, 5)
# print(thistuple[2])             # Ans: ('apple', 'banana', 'cherry')
# print(thistuple[2][0])          # Ans:  apple
# print(thistuple[2][1])          # Ans:  banana
# print(thistuple[2][2])          # Ans:  cherry


# thistuple = (1, 2, ["apple", "banana", "cherry"], 3, 4, 5)
# print(thistuple[2])             # Ans: ('apple', 'banana', 'cherry')
# print(thistuple[2][0])          # Ans:  apple
# print(thistuple[2][1])          # Ans:  banana
# print(thistuple[2][2])          # Ans:  cherry


# # # Syntax: thistuple [start value : end value : increment]
# thistuple = ('a', 'b', 'c', 'd', 'e')
# print(thistuple[1:4:2])         # Ans: ('b', 'd')
# print(thistuple[0:3:1])         # Ans: ('a', 'b', 'c')
#
# thistuple = (1,1,3,2,4)
# print(thistuple)


# # # -------------------------Counting the occurrence of an item in a tuple -----------------------------------
# thistuple = ("apple", "banana", "cherry")
# print(thistuple.count("apple"))             #  Ans: 1

# thislist = [1, 2, 3]
# print(type(thislist))       # Ans : <class 'list'>
#
# thistuple = tuple(thislist)
# print(type(thistuple))      # Ans: <class 'tuple'>
# print(thistuple)            # Ans: (1, 2, 3)

# thattuple = (1, 2, 3)
# print(type(thattuple))      #Ans :  <class 'tuple'>
#
# thatlist = list(thattuple)
# print(type(thatlist))       # Ans: <class 'list'>
# print(thatlist)             # Ans: [1, 2, 3]


# # # -----------------------------------------------------------------------------------------------------------------
# # # --------------------------------------------------Set---------------------------------------------------------
# # # -----------------------------------------------------------------------------------------------------------------

# Set Construction
# Adding an item to a set
# Removing an item from a set
# Changing the value of an existing item of a set
# Accessing the item of a set
# Checking the existence of an item in the set
# Iteration / Looping through the items of a set
# Concatenation of two set
# Finding the length of a set
# Sorting the item of a set
# Reversing  the item in of set
# Counting the occurrence of an item in a set
# Finding the Max and Min value in a set
# Nested set and accessing the items

# # # -----------------------------------Set Construction------------------------------------------------
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = set(("apple", "banana", "cherry"))
# print(thisset)  # Ans: {'apple', 'banana', 'cherry'}

# # # -----------------------------------Adding an item to a set----------------------------------------------
# thisset = {"apple", "banana", "cherry"}
# thisset.add("mango")
# print(thisset)              # Ans: {'cherry', 'mango', 'banana', 'apple'}

# thisset = {"apple", "banana", "cherry"}
# thisset.update("manga", "thenga", "chakka")
# print(thisset)                     # Ans: {'banana', 'm', 'cherry', 'apple', 'n', 'c', 'a', 'g', 't', 'k', 'h', 'e'}


# thisset = {"apple", "banana", "cherry"}
# thisset.update(["manga", "thenga", "chakka"])
# print(thisset)          #Ans : {'manga', 'chakka', 'cherry', 'thenga', 'apple', 'banana'}


# # # -----------------------------------Removing an item from a set----------------------------------------------
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("apple")
# print(thisset)          # Ans : {'cherry', 'banana'}

# thisset = {"apple", "banana", "cherry"}
# thisset.pop(0)
# print(thisset)          # Ans: TypeError: pop() takes no arguments (1 given)

# thisset = {"apple", "banana", "cherry"}
# thisset.pop()
# print(thisset)              # Ans: {'cherry', 'apple'}

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)              # Ans:  set()

#
# thisset = {"apple", "banana", "cherry"}
# del thisset[0]              # Ans: TypeError: 'set' object doesn't support item deletion
#
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)                  # Ans: NameError: name 'thisset' is not defined


# # # -----------------------------------# Accessing the item of a set-------------------------------------------
# thisset = {"apple", "banana", "cherry"}
# print(thisset[0])               #Ans :TypeError: 'set' object does not support indexing

# # # --------------------------------Changing the value of an existing item of a set--------------------------------
# thisset = {"apple", "banana", "cherry"}
# thisset[0] = "mango"            #Ans: TypeError: 'set' object does not support item assignment


# # # --------------------------------Checking the existence of an item in the set--------------------------------

# thisset = {"apple", "banana", "cherry"}
# if "apple" in thisset:
#     print("Yes, apple is there in the fruit set")         # Ans: Yes, apple is there in the fruit set

# # # --------------------------------Iteration / Looping through the items of a set------------------------------
# thisset = {"apple", "banana", "cherry"}

# for i in thisset:
#     print(i)

# # # --------------------------------Concatenation of two set------------------------------
#
# thisset = {"apple", "banana", "cherry"}
# thatset = {"manga", "thenga", "chakka"}
# bigset = thisset + thatset
# print(bigset)               # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# # # --------------------------------Finding the length of a set------------------------------
#
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))         # Ans: 3

# # # -------------------------------Sorting the item of a set------------------------------
# thisset = {"apple", "banana", "cherry"}
# print(thisset.sor)

# # # -------------------------------Reversing  the item in of set-----------------------------
# # Not applicable

# # # ----------------------Counting the occurrence of an item in a set------------------------------------
# # Not applicable

# # # --------------------Finding the Max and Min value in a set-----------------------------------
# # Not applicable


# # # -------------------Nested set and accessing the items----------------------------------

thisset = {1, 2, 3, {"apple", "banana", "cherry"}}
print(thisset)              # Ans: TypeError: unhashable type: 'set'
