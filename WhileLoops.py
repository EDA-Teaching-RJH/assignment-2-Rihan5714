import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = None

print("Try and beat the Guessing Game!!!")
print("I have chosen a random number between 1 and 100. Can you guess it?")

# Use a while loop to keep asking for guesses
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))  # Ask for user input
        if guess < secret_number:
            print("Too low! Guess again!")
        elif guess > secret_number:
            print("Too high! Guess again!")
        else:
            print("Congrats, you got the number correct!")
    except ValueError:
        print("Please enter a number between 1 and 100.")

