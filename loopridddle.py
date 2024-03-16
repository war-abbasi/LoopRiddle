import random

print("Welcome to LoopRiddle!")
print("Guess the secret number between 1 and 100.")
print("You have 5 attempts.\n")

secret_number = random.randint(1, 100)
attempts = 0

while attempts < 5:
   guess = int(input("Enter your guess: "))
   attempts += 1

   if guess == secret_number:
       print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
       break
   elif guess < secret_number:
            print("Too low. Try again.")
   else:
            print("Too high. Try again.")

else:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

