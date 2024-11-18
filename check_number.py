

# first create function check_num
# add parameter num
# write if statement
# check first num is 0 
# else num is positive
# else num is negative
# print result


def check_num(num):
    if num == 0:
        result = "Number is 0"
    elif num >= 1:
        result = "Number is Positive"
    else:
        result = "Number is Negative"
    return result


number = int(input("Enter Number to check:"))


print(check_num(number))

