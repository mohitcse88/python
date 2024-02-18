# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: ")


# This is not optimized becasue in every condition lenght will be calculated
# if len(password) < 6:
#     strenght = "week"
# elif len(password) <= 10:
#     strenght = "medium"
# else:
#     strenght = "strong"


# This is optimized because here lenght will once calculated
# if you write optimized code like this then you become a production level coder 
password_lenght = len(password)

if password_lenght < 6:
    strenght = "week"
elif password_lenght <= 10:
    strenght = "medium"
else:
    strenght = "strong"

print("Your password strenght is "+ strenght)