
num = 3
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 3

    conversion_factor = 2.54

    while True:
        inches = float(input("Enter a value in inches (negative value to quit): "))

        if inches < 0:
            print("Negative value entered. Program will end.")
            break
        centimeters = inches * conversion_factor
        print(f"{inches} inches is equal to {centimeters} centimeters.")

        numbers = []

        while True:
            user_input = input("Enter a number (or press Enter to quit): ")
            if user_input == "":
                break

            try:
                number = float(user_input)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        if numbers:
            print(f"The smallest number is: {min(numbers)}")
            print(f"The largest number is: {max(numbers)}")
        else:
            print("No numbers were entered.")

            import random
            number_to_guess = random.randint(1, 10)
            while True:
                user_input = input("Guess a number between 1 and 10: ")

                try:
                    guess = int(user_input)
                    if guess < number_to_guess:
                        print("Too low!")
                    elif guess > number_to_guess:
                        print("Too high!")
                    else:
                        print("Correct! You've guessed the number!")
                        break
                except ValueError:
                    print("Please enter a valid number between 1 and 10.")


correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left.")

    if attempts == max_attempts:
        print("Access denied")

import random
def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    pi_approximation = 4 * points_inside_circle / num_points
    return pi_approximation

def main():
    num_points = int(input("Enter the number of random points to generate: "))

    pi_value = approximate_pi(num_points)

    print(f"Approximation of pi using {num_points} points: {pi_value}")
if __name__ == "__main__":
    main()





