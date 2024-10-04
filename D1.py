'''class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def __str__(self):
        return (f"Car Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")
def main():
    my_car = Car("ADD-7793", 150)
    print(my_car)
if __name__ == "__main__":
    main()


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def __str__(self):
        return (f"Car Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")


def main():
    my_car = Car("ADD-7793", 150)
    my_car.accelerate(25)
    print(f"Current speed after accelerating +30 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(70)
    print(f"Current speed after accelerating +70 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(50)
    print(f"Current speed after accelerating +50 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(-200)
    print(f"Final speed after emergency brake: {my_car.current_speed} km/h")
if __name__ == "__main__":
    main()


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number  # Registration number of the car
        self.max_speed = max_speed  # Maximum speed of the car in km/h
        self.current_speed = 0  # Current speed of the car in km/h
        self.travelled_distance = 0  # Travelled distance of the car in km

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

    def __str__(self):
        return (f"Car Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")


def main():
    my_car = Car("ADD-7793", 150)

    my_car.accelerate(30)
    print(f"Current speed after accelerating +30 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(70)
    print(f"Current speed after accelerating +70 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(50)
    print(f"Current speed after accelerating +50 km/h: {my_car.current_speed} km/h")
    my_car.drive(1.5)
    print(f"Travelled distance after driving for 1.5 hours: {my_car.travelled_distance} km")
    my_car.accelerate(-200)
    print(f"Final speed after emergency brake: {my_car.current_speed} km/h")
    my_car.drive(1)
    print(f"Travelled distance after driving for 1 hour: {my_car.travelled_distance} km")
if __name__ == "__main__":
    main()

import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

    def __str__(self):
        return (f"{self.registration_number:<10} | "
                f"{self.max_speed:<12} | "
                f"{self.current_speed:<14} | "
                f"{self.travelled_distance:<20}")


def main():
    cars = []

    for i in range(1, 11):
        reg_number = f"ADD-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg_number, max_speed))
    print(f"{'Registration':<10} | {'Max Speed':<12} | {'Current Speed':<14} | {'Distance Travelled':<20}")
    print("-" * 60)
    race_in_progress = True
    hours = 0

    while race_in_progress:
        hours += 1

        for car in cars:

            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_in_progress = False
                break

    for car in cars:
        print(car)

if __name__ == "__main__":
    main()

class InsufficientFundsError(Exception):
    pass

class NegativeValueError(Exception):
    pass

def main():
    while True:
        try:
            balance_input = input("Enter your account balance: ")
            balance = float(balance_input)

            if balance < 0:
                raise NegativeValueError("Balance cannot be negative.")

            withdrawal_input = input("Enter the withdrawal amount: ")
            withdrawal_amount = float(withdrawal_input)


            if withdrawal_amount < 0:
                raise NegativeValueError("Withdrawal amount cannot be negative.")
            if withdrawal_amount > balance:
                raise InsufficientFundsError("Withdrawal amount exceeds account balance.")
            balance -= withdrawal_amount
            print(f"Withdrawal successful! Your new balance is: {balance:.2f}")
            break

        except ValueError:
            print("Invalid input. Please enter numeric values for balance and withdrawal.")
        except InsufficientFundsError as e:
            print(e)
        except NegativeValueError as e:
            print(e)
if __name__ == "__main__":
    main()'''


def write_notes(filename):
    with open(filename, 'w') as file:
        while True:
            note = input("Enter a new note (or type 'exit' to stop): ")
            if note.lower() == 'exit':
                break
            file.write(note + '\n')
    print("Notes have been written to the file.")


def read_notes(filename):
    try:
        with open(filename, 'r') as file:
            notes = file.readlines()
            if notes:
                print("Existing notes:")
                for note in notes:
                    print(note.strip())
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("The file does not exist.")


def append_notes(filename):
    with open(filename, 'a') as file:
        while True:
            note = input("Enter a note to append (or type 'exit' to stop): ")
            if note.lower() == 'exit':
                break
            file.write(note + '\n')
    print("Additional notes have been appended to the file.")


def main():
    filename = "notes.txt"

    while True:
        print("\nMenu:")
        print("1. Write new notes")
        print("2. Read existing notes")
        print("3. Append additional notes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            write_notes(filename)
        elif choice == '2':
            read_notes(filename)
        elif choice == '3':
            append_notes(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()





