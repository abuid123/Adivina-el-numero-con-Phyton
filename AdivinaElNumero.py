# Este es el juego de adivinar el numero
import random

guessesTaken = 0
minNumber = 1
maxNumer = 20

print("Hello, What is your name?: ")
username = input()

number = random.randint(minNumber, maxNumer)
print("Well, " + username + ". I am thinking in a number between 1 and 20")

#Bucle del juego
while guessesTaken < 6:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("You guess is too low.")

    if guess > number:
        print("You guess is too high.")

    if guess == number:
        break;

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good Job. " + username + "! you guessed my number in " + guessesTaken + " guesses!")
if guess != number:
    number = str(number)
    print("No, the number I was thinking of was " + number)
