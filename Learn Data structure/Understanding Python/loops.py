# # # -------------------------------------while loop----------------------------------------------

# # # indefinite loop
# i = 1
# while i < 10:
#     print(i)

# # # Definite loop
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1     # This can  be writer lik this also -->   i += 1     # # Ans: 1,2,3,4,5,6,7,8,9

# # # Use of the break statement
# i = 1
# while i < 10:
#     print(i)
#     if i == 8:
#         break
#     i = i + 1                   # # Ans: 1,2,3,4,5,6,7,8

# # # Use of the continue statement
# i = 1
# while i < 10:
#     print(i)
#     if i == 8:
#         continue
#     i = i + 1                   # # Ans:  1,2,3,4,5,6,7,8,8,8,8,8,8,8.......


# # # There for we have to modify the code , so that we wont get a indefinite loop
# i = 1
# while i < 10:
#     i = i + 1
#     if i == 8:
#         continue
#     print(i)                       # # Ans:  2,3,4,5,6,7,9,10

# # # But we expect the answer to be like 1,2,3,4,5,6,7,9     -> for that we have to modify the stating and end value
# i = 0
# while i < 9:
#     i = i + 1
#     if i == 8:
#         continue
#     print(i)                      # # Ans:  1,2,3,4,5,6,7,9


# # # ---------------------------------------------------------------------------------------------
# # # ---------------------------------------------------------------------------------------------
# # # -------------------------------------range function ------------------------------------------

# # # Syntax ----> range (start value, end value , increment value)

# for i in range(10):
#     print(i)  # range(0,10)this is in the form of index->so start value is 0 and end value will be 9 that is(10-1=9)
#                 # # Ans :  0,1,2,3,4,5,6,7,8,9

# for i in range(1, 5):
#     print(i)       # # Ans :  1,2,3,4

# # # Q.Write a python program to print all odd numbers in between 1 to 10
# for i in range(1, 10, 2):
#     print(i)  # # Ans :  1,3,5,7,9

# # # Q.Write a python program to print all even numbers in between 1 to 10
# for i in range(2, 10, 2):
#     print(i)  # # Ans :  2,4,6,8


# # # What will happen if we give high start value and low end value
# for var in range(20,10,2):
#     print(var)


# # # # break statement in a for loop
# for i in range(1, 10, 2):
#     print(i)
#     if i == 5:
#         break             # Ans : 1,3,5

# # # continue statement in a for loop
# for i in range(1, 10, 2):
#     print(i)
#     if i == 5:
#         continue            # Ans : 1,3,5,7,9



