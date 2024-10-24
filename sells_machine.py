# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins 
# in these denominations: 25 cents, 10 cents, and 5 cents. Implement a program that prompts the 
# user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


reserved_coin = [25,10,5]
tot_coin = 0
tot_required = 50

while(True):
    coin = int(input("Enter a coin: "))
    try:
        if coin in reserved_coin:
            tot_coin += coin
    except:
        # To be ignored!!
        continue

    if tot_required <= tot_coin :
        #The user inputed atleast 50 Cents
        print(f"Finished!! we owe you {tot_coin - tot_required} cent(s).")
        break
    if coin in reserved_coin:
        # Informing the user amount due so far
        print(f"Amount due is {tot_required - tot_coin}")
        continue
   

