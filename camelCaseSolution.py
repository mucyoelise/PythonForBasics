camel_case = input("Enter a name of variable in camel case: ")
print("A name of variable given in snake_case: ", end = "")
for letter in camel_case:
    if letter.isupper():
        print("_", end = "")
        letter = letter.lower()
    print(letter, end = "")
