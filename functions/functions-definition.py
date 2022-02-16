# function definition
# sum
def sum_two_number(first, second):
    return (first + second)

sum_result = sum_two_number(1, 2)
print(sum_result)

# function definition
# print_text(arg1, arg2)
def print_text(fname, lname):
    return ("My name is " + fname + " " + lname)

print(print_text("Nhan", "Nguyen"))

# function definition
# sum(*arg) - *arg are unknown number of arguments
def sum_numbers(*num):
    return sum(num)

print(sum_numbers(10, 11, 12, 13, 14, 15))

# function definition
# average(*arg) - *arg are unknown number of arguments
def avg_numbers(*num):
    return sum(num) / len(num)

print(avg_numbers(10, 11, 12, 13, 14, 15))

# function definition
# my_function(**kid) - **kid are unknown number of keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# function definition
# default argument
def country_function(country = "Norway"):
  print("I am from " + country)

country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil")

# function definition
# define function without statement
def blank_function():
  pass