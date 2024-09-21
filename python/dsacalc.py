
Num1 = float(input("Enter your First Number :- "))
Symbol = str(input("Enter Your Calculat Symbol Like(+,-,*,/,%) :- "))
Num2 = float(input("Enter Your Second Number :- "))

if Symbol == "+":
    print(f"\n Your First Number Is = {Num1}\n Your Second Number Is = {Num2}\n The Anser Is = {Num1 + Num2}")
elif Symbol == "-":
        print(f"\n Your First Number Is = {Num1}\n Your Second Number Is = {Num2}\n The Anser Is = {Num1 - Num2}")
elif Symbol == "*":
        print(f"\n Your First Number Is = {Num1}\n Your Second Number Is = {Num2}\n The Anser Is = {Num1 * Num2}")
elif Symbol == "/":
        print(f"\n Your First Number Is = {Num1}\n Your Second Number Is = {Num2}\n The Anser Is = {Num1 / Num2}")
elif Symbol == "%":
          print(f"\n Your First Number Is = {Num1}\n Your Second Number Is = {Num2}\n The Anser Is = {Num1 % Num2}")
else :
    pass