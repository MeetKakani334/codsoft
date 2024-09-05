def voting_systum():
    BJP = 0
    CON = 0
    AAP = 0
    while True:
        vot = input("Enter Your Vot").upper()
        if vot == "BJP":
            BJP+=1
        elif vot == "CON":
            CON+=1
        elif vot == "AAP":
            AAP+=1
        elif vot == "EXIT":
            break
        else :
            print("Enter Valid Party")
    if BJP>CON and BJP>AAP:
        print("BJP WON")
    elif CON>BJP and CON>AAP:
        print("CON WON")
    elif AAP>BJP and AAP>CON:
        print("AAP WON")
  # elif BJP == CON or BJP == AAP or CON == AAP:
    #     print("VOTE AGAIN")

    else:
        pass
        
    print("BJP:",BJP)
    print("CON",CON)
    print("AAP",AAP)
    

voting_systum()
