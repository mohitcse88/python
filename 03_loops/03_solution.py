# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the number: "))

for i in range(1,11):
    if i == 5:
        continue
    print(number, "X", i, "=", number*i)