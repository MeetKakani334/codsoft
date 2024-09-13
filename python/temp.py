def convert_temp():
    try:
        choice = input("convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? enter C & F ").upper()
        if choice == "C":
            celsius = float(input("Enter Temperature In Celsius"))
            fahrenheit = (celsius * 9/5)+32
            print(f"{celsius}C is equal to {fahrenheit}")
        elif choice == "F":
            fahrenheit = float(input("Enter Temperature In Fahrenheit"))
            celsius = (fahrenheit-32)*5/9
            print(f"{ fahrenheit}F is equal to {celsius}")
        else:print("Enter valid temp")
    except ValueError:print("invalid c or f")
    finally:print("thank you")
convert_temp()

        
