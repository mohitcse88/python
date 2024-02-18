# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter your pet sepecies: ").lower()
age = int(input("Enter the age of you pet: "))

food = ""
if pet == "dog":
    if age < 2:
        food = "Puppy food"
elif pet == "cat":
    if age > 5 :
        food = "Senior cat food"
else:
    print("I have not information about", pet, "food")

print("AI recomend to give "+ food + " to your pet")