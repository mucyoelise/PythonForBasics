# When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
# as by omitting vowels, much like Twitter was originally called .  Implement a program
# that prompts the user for a str of text and then outputs that same text but with all 
# vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. 


 
word = input("Enter a string: ")
print("Word with vowels omitted: ", end="")
for letter in word:
    if letter.lower() in ["a", "e", "i", "u", "o"]:
        continue
    else:
        print(letter, end="")
    