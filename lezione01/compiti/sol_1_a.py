print("Welcome! Insert your informations.\n")

name = input("Insert your name: ")
surname = input("Insert your surname: ")
age = int(input("Insert your age: "))

if len(name) > 1 and name[0].isupper() and len(surname) > 1 and surname[0].isupper() and age >= 18:
    print("\nLogged in successfully!\n")
    print(f"Your name is '{name}', your surname is '{surname}' and your age is '{age}'.")
else:
    print("Login failed. Some data are incorrect!")
