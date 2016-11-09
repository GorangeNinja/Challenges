vowels = "aeiou"
list2 = ""

user = input()

for char in user:
    for char2 in vowels:
        if char == char2: list2 += char

for char2 in vowels:
    user = user.replace(char2, "")
    
user = user.replace(" ","")

print(user, list2)