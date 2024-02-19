# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter the number: "))

sum_even = 0
for number in range(1, n+1):
    if number % 2 == 0:
        # sum_even = sum_even + 1
        sum_even+=1

print("The sum of even number is: ", sum_even)