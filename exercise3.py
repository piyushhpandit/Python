# name = input("Enter your name")
# ltr = input("Enter a letter")
# print(len(name))
# print(ltr.count(""))

# SOLUTION 

name, char = input("enter comma seperated name and character :").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")


