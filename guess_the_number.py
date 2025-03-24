import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guess_the_number()