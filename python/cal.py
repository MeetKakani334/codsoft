def calclutor():
    try:
        NUMBER1 = float(input("Enter Your First Number"))
        SIGN = input("Enter YOUR SIGN")
        NUMBER2 = float(input("Enter Your Second Number"))
        if SIGN == "+":
            print(NUMBER1 + NUMBER2)
        elif SIGN == "-":
            print(NUMBER1 - NUMBER2)
        elif SIGN == "*":
            print(NUMBER1 * NUMBER2)
        elif SIGN == "/":
            print(NUMBER1 / NUMBER2)
        else:
            print(" invalid sign")
    except ValueError:
        print("Error : Pls Enter Valid Sign")
    finally:
        print("Thankyou")
calclutor()
