def run():

    def celsius_to_fahrenheit(c):
        """convert Celsius to Fahrenheit."""
        resultat = round(c * 9 / 5 + 32, 1)
        return resultat
    
    def fahrenheit_to_celsius(f):
        """convert Fahrenheit to Celsius."""
        return round((f - 32) * 5 / 9, 1)
    
    while True:
        user_choice = input(""" === Converter ===
        (1) Celsius → Fahrenheit
        (2) Fahrenheit → Celsius
        (0) Quit 
        """)
        if user_choice == "1":
            c = float(input("Temperature: "))
            print(f"{celsius_to_fahrenheit(c)} °F")
        elif user_choice == "2":
            f = float(input("Temperature: "))
            print(f"{fahrenheit_to_celsius(f)} °C")
        elif user_choice == "0":
            break
        else:
            print("Please, write '1' for Celsius → Fahrenheit or '2' for Fahrenheit → Celsius.")

if __name__ == "__main__":
    run()