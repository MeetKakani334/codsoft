# def voting_systum():
#     BJP = 0
#     CON = 0
#     AAP = 0
#     while True:
#         vot = input("Enter Your Vot").upper()
#         if vot == "BJP":
#             BJP+=1
#         elif vot == "CON":
#             CON+=1
#         elif vot == "AAP":
#             AAP+=1
#         elif vot == "EXIT":
#             break
#         else :
#             print("Enter Valid Party")
#     if BJP>CON and BJP>AAP:
#         print("BJP WON")
#     elif CON>BJP and CON>AAP:
#         print("CON WON")
#     elif AAP>BJP and AAP>CON:
#         print("AAP WON")
#     elif BJP == CON and BJP == AAP and CON == AAP:
#         return voting_systum()
#     else:
#         pass
        
#     print("BJP:",BJP)
#     print("CON",CON)
#     print("AAP",AAP)
    

# voting_systum()


def voting_system():
    while True:
        # Initialize vote counts
        BJP = 0
        CON = 0
        AAP = 0

        # Conduct voting
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

        # Check if there's a tie between all three parties
        if BJP == CON == AAP:
            print("It's a tie between all three parties!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  # Restart the voting process

        # Check for tie between two parties
        if BJP == CON and BJP > AAP:
            print("BJP and CON are tied!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  # Restart the voting process
        elif BJP == AAP and BJP > CON:
            print("BJP and AAP are tied!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  # Restart the voting process
        elif CON == AAP and CON > BJP:
            print("CON and AAP are tied!")
            print("BJP:", BJP, "CON:", CON, "AAP:", AAP)
            print("Restarting voting...\n")
            continue  # Restart the voting process

        # Determine the result based on the vote counts
        if BJP > CON and BJP > AAP:
            print("BJP WON")
        elif CON > BJP and CON > AAP:
            print("CON WON")
        elif AAP > BJP and AAP > CON:
            print("AAP WON")

        # Print the vote counts
        print("Final vote counts:")
        print("BJP:", BJP)
        print("CON:", CON)
        print("AAP:", AAP)

        # Exit the loop if a definitive winner is found (no ties)
        break

# Start the voting system
voting_system()





