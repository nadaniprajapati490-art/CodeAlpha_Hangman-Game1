import random

# List of words
words = ["python", "college", "student", "computer", "coding"]

# Random word selection
word = random.choice(words)

guessed = []
wrong = 0
limit = 6

print("=== Hangman Game ===")

while wrong < limit:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("🎉 Congratulations! You Win!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        wrong += 1
        print("Wrong Guess!")
  …
