import random

# Generate a random number between 1 and 50
random_num = random.randint(1, 50)

while True:  # Start an infinite loop for continuous guessing
    user_input = input("Guess the Number (1-50): ")

    # Check if the input is a valid number
    if user_input.isdigit():
        guess_number = int(user_input)

        if 1 <= guess_number <= 50:
            if guess_number == random_num:
                print("Congratulations! You guessed the correct number!")
                break  # Exit the loop since the correct number was guessed
            elif guess_number < random_num:
                print("Your guess is below the number.")
            else:
                print("Your guess is above the number.")
        else:
            print("Please enter a number between 1 and 50.")
    else:
        print("Please enter a valid number.")

# The loop will continue until the correct number is guessed

