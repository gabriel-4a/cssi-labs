print("Welcome to Gabriel's Function Calculator")

num1 = int(raw_input("Give me a number please: "))
num2 = int(raw_input("Give me another number please: "))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum

print("Here is the sum: " + str(myAddFunction(num1, num2)))



def mySubtractFunction(sub1, sub2):
    dif = sub1 - sub2
    return dif

print("Here is the difference: " + str(mySubtractFunction(num1, num2)))



def myMultFunction(mult1, mult2):
    product = mult1 * mult2
    return product

print("Here is the product: " + str(myMultFunction(num1, num2)))
