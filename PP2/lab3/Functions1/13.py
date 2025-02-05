import random

print("Hello! What is your name?")
name = input()

secret_number = random.randint(1, 20)
print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

x = 0

while True:
    print("\nTake a guess.")
    guess = int(input())
    x += 1
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {x} guesses!")