def voting_system():
    while True:

        BJP = 0
        CON = 0
        AAP = 0

        while True:
            vote = input("Enter your vote (BJP, CON, AAP) or type 'EXIT' to finish: ").upper()
            if vote == "BJP":
                BJP += 1
            elif vote == "CON":
                CON += 1
            elif vote == "AAP":
                AAP += 1
            elif vote == "EXIT":
                break
            else:
                print("Invalid input. Please enter a valid party name (BJP, CON, AAP) or 'EXIT' to finish.")


        if BJP == CON == AAP:
            print("It's a tie between all three parties!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  

        if BJP == CON and BJP > AAP:
            print("BJP and CON are tied!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue 
        elif BJP == AAP and BJP > CON:
            print("BJP and AAP are tied!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  
        elif CON == AAP and CON > BJP:
            print("CON and AAP are tied!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  

        if BJP > CON and BJP > AAP:
            print("BJP WON")
        elif CON > BJP and CON > AAP:
            print("CON WON")
        elif AAP > BJP and AAP > CON:
            print("AAP WON")

        print("Final vote counts:")
        print("BJP:", BJP)
        print("CON:", CON)
        print("AAP:", AAP)

        break

voting_system()





