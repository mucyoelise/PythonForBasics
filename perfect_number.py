nbrs = int(input("Enter a number to find its less perfect numbers: "))
pfct_counter = 0
for nbr in range(nbrs):
    number = nbr
    total = 0
    for i in range(number):
        if i == 0:
            continue
        else:
            if (number/i).is_integer() :
                total += i

            if total == number and i == number - 1:
                print(f"{number} is a perfect number!")
                pfct_counter += 1
                break    
print(f"Thus, there is/are {pfct_counter} perfect number(s) less than the provided number!")