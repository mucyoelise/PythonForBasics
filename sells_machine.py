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
   

