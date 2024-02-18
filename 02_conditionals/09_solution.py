# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# how to finde leap year 
year = int(input("Enter the year: "))

# if we check two condition then wrap it inside () because in this condition parenthesis is important
# if (year % 4 == 0 and year % 100 != 0):
if  (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")