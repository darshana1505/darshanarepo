import random


def roll_dice():
    return random.randint(1, 6)


def main():
    while True:
        result = roll_dice()
        print(f"You rolled: {result}")
        if result == 6:
            print("You rolled a 6! Stopping the rolls.")
            break
if __name__ == "__main__":
    main()

import random


def roll_dice(sides):
    return random.randint(1, sides)


def main():

    sides = int(input("Enter the number of sides on the dice: "))

    while True:
        result = roll_dice(sides)
        print(f"You rolled: {result}")
        if result == sides:
            print(f"You rolled a {sides}! Stopping the rolls.")
            break
if __name__ == "__main__":
    main()


def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters


def main():
    while True:
        user_input = input("Enter the volume in gallons (negative value to quit): ")

        try:
            gallons = float(user_input)
            if gallons < 0:
                print("Negative value entered. Exiting the program.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()


def sum_of_list(numbers):
    total = sum(numbers)
    return total


def main():
    test_list = [10, 20, 30, 40, 50]

    total_sum = sum_of_list(test_list)

    print(f"The sum of the list {test_list} is: {total_sum}")


if __name__ == "__main__":
    main()


def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


def main():
    original_list = [10, 21, 32, 43, 54, 65, 76, 87, 98]

    filtered_list = remove_odd_numbers(original_list)

    print(f"Original list: {original_list}")
    print(f"List without odd numbers: {filtered_list}")
if __name__ == "__main__":
    main()

import math


def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    area_square_meters = area / 10000
    unit_price = price / area_square_meters
    return unit_price

def main():
    print("Enter details for Pizza 1:")
    diameter1 = float(input("Diameter (cm): "))
    price1 = float(input("Price (€): "))

    print("Enter details for Pizza 2:")
    diameter2 = float(input("Diameter (cm): "))
    price2 = float(input("Price (€): "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"\nUnit price for Pizza 1: €{unit_price1:.2f} per square meter.")
    print(f"Unit price for Pizza 2: €{unit_price2:.2f} per square meter.")

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


if __name__ == "__main__":
    main()










