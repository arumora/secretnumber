secret = 15

guess = int(input("Guess the secret number (between 1 and 30): "))

if guess == secret:
    print("You've guessed it! Congratulations! It's number 15.")
else:
    print("Unfortunately, your guess is not correct. The secret number is not " + str(guess) + ".")