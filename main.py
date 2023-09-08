# Beschreibung: Spiel "Guess the Number"
# einbinden der random library
import random

# Funktion zum erraten der Zahl
def guess_the_number():
    # Zufallszahl zwischen 1 und 100 generieren und in der Variable number speichern
    number = random.randint(1, 100)
    # Anzahl der Versuche auf 0 setzen
    attempts = 0
#comm
    print("I've chosen a number between 1 and 100. Try to guess it!")

    # Schleife, die solange läuft, bis die Zahl erraten wurde, oder das Programm durch eine Exception beendet wird
    while True:
        #Try-Except Block, um eine Exception abzufangen, falls der User keine Zahl eingibt
        try:
            # User Eingabe und umwandeln in Integer speichern in der Variable guess
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
                #mit break wird die Schleife beendet
                break
        except ValueError:
            print("Please enter a valid number.")
            exit(1)

# Main Funktion
if __name__ == "__main__":
    # Aufruf der Funktion guess_the_number()
    guess_the_number()

