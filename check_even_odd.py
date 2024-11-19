

#check even odd num

#first need function check_num with num parameter 
#with if statement i have to perform 1 operation 
# num % 0 === 0 if true else false
# return result

def check_num(num):
    if num % 2 == 0:
        result = "Number is Even"
    else: 
        result = "Number is Odd"
    return result
num = 3
print(check_num(num))

