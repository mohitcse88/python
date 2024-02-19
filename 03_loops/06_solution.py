# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter the number: "))
factorial = 1

while number > 0:
    # factorial = factorial * number # not optimized
    # number = number -1 
    factorial *= number # optimized
    number -= 1
print("Factorial value of ", number , "is: ", factorial)


# not optimized
# i = 1
# while i < number + 1:
#     factorial *= i
#     i+=1
# print("Factorial of ",number,"is : ",factorial)