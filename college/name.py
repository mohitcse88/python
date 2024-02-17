user = input("Enter your name: ")
user= user.lower()
words = user.split()

if "name" and "is" in user:
    name_index = words.index("name")
    try:
        if "is" == words[name_index+1]:
            print(words[name_index+2])
    except:
        if "is" == words[name_index-2]:
            print(words[name_index-3])
elif len(words) == 1:
    print(words[0])
elif "i" and "am" in user:
    am_index = words.index("am")
    print(words[am_index+1])
elif "this" and "side" in user:
    side_index = words.index("side")
    print(words[side_index+1])
    








