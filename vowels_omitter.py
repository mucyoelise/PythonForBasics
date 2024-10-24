word = input("Enter a string: ")
print("Word with vowels omitted: ", end="")
for letter in word:
    if letter.lower() in ["a", "e", "i", "u", "o"]:
        continue
    else:
        print(letter, end="")
    