

def square(n):
  return n*n
def cube(n):
  return n**3

number = int(input("Enter number to find square root:"))
print("Square root of {1} is {0}".format(square(number), number))
print("Cube root of {num} is {num_cube}".format(num_cube=cube(number), num=number))