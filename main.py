import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    print("I've chosen a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Your guess: "))

            # Check if the guess is within the range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Increment the number of attempts
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
            exit(1)

if __name__ == "__main__":
    guess_the_number()

