# find largest number in three 

# we need to find lagest num from numbers

# there are 3 numbers
# create  function largest_num 
# add parameter a,b,c or n1,n2,n3
# write if statement and we have to perform 2 operations
# a < b and a < c result = a / inside a function declare result variable
# c < b result = b
# result = c
# return result
# outsied define a variable number and assign built in function int with inside input to take input
# print result

#edge case if number is equal then equal number will be largest
def largest_num(a,b,c):
    if c < a and b < a:
        result = f"Largest Number is : {a}"
    elif c < b:
        result = f"Largest Number is : {b}"
    else:
        result = f"Largest Nuber is : {c}"
    return result

number_one = int(input("Enter first Number : "))
number_two = int(input("Enter second Number : "))
number_three = int(input("Enter third Number : "))

print(largest_num(number_one,number_two,number_three))






