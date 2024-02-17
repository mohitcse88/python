# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Provide me your age: "))
day = input("Provide me a day: ")[0:1].lower() # we are storing first character of day because only wednesday starting from "w"

price = 18 if age >= 18 else 8

if day == "w":
    # price = price -2
    price -= 2

print("Ticket price for you is $", price)
