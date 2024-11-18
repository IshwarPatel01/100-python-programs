#multiplication table

# first i need concatenation for design table in cli
# take input form user for num1 and upto to complete table
# create function multiplication_table
# add 2 parameter num, upto
# define loop to itrate 10 times 
# inside loop declare variable with name multiply
# and return variable
# outside function declare 1 variables number for taking input through cli,user
# print result

# in this i made algorithmatic mistake
# also implimentation mistake
def mulitilpication_table(num, upto = 10):
    for i in range(1,upto + 1):
        multiply = i * num 
        result = f"{i} * {num} = {multiply}" 
        print(result) 

number_one = int(input("Enter First Number of Multiplication : "))

print(mulitilpication_table(number_one))
