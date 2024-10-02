import random
nummber_to_guss = random.randint(1,100)
guss = None
while nummber_to_guss != guss:
    guss = int(input("enter youre number in to 1 to 100"))
    if guss < nummber_to_guss:
        print("this is low number")
    elif guss > nummber_to_guss:
        print("hig number")
    else:
        print("cong")
        break