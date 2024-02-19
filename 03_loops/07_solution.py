# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10


while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
    else:
        print("Invalid number , try again")





# number = int(input("Enter the number: "))

# i = 1
# while  i:
#     print(number)
#     number = int(input("Enter the number: ")) # this optimized because after enter the number codition will be check and break 
    # if number >= 1 and number <= 10:
    #     break
    # number = int(input("Enter the number: ")) 
    # this is not optizmized because after enter number again comes in while loop then check codition 


