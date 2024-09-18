'''file = open("example.txt","w")
file.write("Life is beautiful")
file.close()


file = open("example.txt", "r")
content =  file.read()
print(content)
file.close()
file  = open("example.txt", "a")
file.write("\ndarshana")
file.close()
with open("example.txt", "r") as file:
    content = file.read()
    print(content)'''
'''try:
     num1 = int(input("Enter the first number: "))
     num2 = int(input("Enter the second number: "))
     result = num1 / num2
     print(f"result: {result}")
except Exception as e:
    print(f"Error: {e}")'''
'''class Dog:
    pass
dog = Dog()
dog.name = "Bubbles"
dog.birth_year = 2022
print(f"{dog.name} is {dog.birth_year}.")'''
'''class Dog:
    def __init__(self, name, birth_year, sound="Woof Woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return
dog1 = Dog("Rascal" , 2018)
dog2 = Dog("Boi" , 2022, "Yip yop yip")

dog1.bark(2)
dog2.bark(5)

class Dog:
    created = 0
    def __init__(self, name, birth_year, sound="Woof Woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        dog.created = Dog.created + 1

    dog1 = Dog("Rascal" , 2018)
    dog2 = Dog("Boi" , 2022, "Yip yop yip")
    dog3 = Dog("Rascal" , 2018)
'''



seasons = ("Winter", "Spring", "Summer", "Autumn")
month = int(input("Enter the month number (1-12): "))
if month in (12, 1, 2):
    season = seasons[0]
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[2]
elif month in (9, 10, 11):
    season = seasons[3]
else:
    season = "Invalid month"
print(f"The season for month {month} is: {season}")






names = set()

while True:
    name = input("Enter a name (or press Enter to finish): ")


    if name == "":
        break


    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)


print("\nNames entered:")
for name in names:
    print(name)


    airports = {}

    while True:

        print("\nMenu:")
        print("1. Enter a new airport")
        print("2. Fetch an existing airport")
        print("3. Quit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            icao_code = input("Enter the ICAO code of the airport: ").upper()
            if icao_code in airports:
                print(f"Airport with ICAO code {icao_code} already exists.")
            else:
                airport_name = input("Enter the name of the airport: ")
                airports[icao_code] = airport_name
                print(f"Airport {airport_name} with ICAO code {icao_code} added.")

        elif choice == "2":
            icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()
            if icao_code in airports:
                print(f"The name of the airport with ICAO code {icao_code} is {airports[icao_code]}.")
            else:
                print(f"No airport found with ICAO code {icao_code}.")

        elif choice == "3":
            print("Quitting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")