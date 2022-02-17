# for loop, print elements in list
# fruits = ["apple", "banana", "cherry", "mango"]
# for x in fruits:
#   print(x)

# for loop, print elements in tuple
# fruits = ("apple", "banana", "cherry", "mango")
# for x in fruits:
#   print(x);

# with the continue statement we can stop the current iteration of the loop, and continue with the next: 
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# exit the loop when x is "banana":
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# exit the loop when x is "banana", but this time the break comes before the print:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# using the range() function:
# for x in range(5):
# for x in range(2, 5):
#   print(x)

# print all numbers from 0 to 5, and print a message when the loop has ended:
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# nested for loop
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for a in adj:
#     for b in fruits:
#         print(a , b)

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
# for x in [0, 1, 2]:
#   pass