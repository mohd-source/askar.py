import random

# Word lists
easy_words = ["apple", "banana", "orange", "money", "india"]
medium_words = ["computer", "keyboard", "laptop", "internet", "software"]
hard_words = ["programming", "mountain", "elephant", "debugging", "diamond"]

print("Welcome to the Word Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

level = input("Enter the level (1 - 3): ")

if level == '1':
    word = random.choice(easy_words)
elif level == '2':
    word = random.choice(medium_words)
elif level == '3':
    word = random.choice(hard_words)
else:
    print("Invalid level selected. Defaulting to Easy.")
    word = random.choice(easy_words)

attempts = 0

# Main game loop
while True:
    print("Guess the secret Word!")
    print(f"Hint: {word[0]}{'_' * (len(word)-1)}")  # Show first letter as initial hint
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if guess == word:
        print(f"Congratulations! You've guessed the password '{word}' in {attempts} attempts.")
        break
    choice1=input("Do you want Hint? (yes/no): ").lower()
    
    if choice1=="yes":
        hint = word[0]  # first letter always given
        for i in range(1, len(word)):
            if i < len(guess) and guess[i] == word[i]:
                hint += word[i+1]
            else:
                hint += "_"
        print(f"Hint: {hint}")
    else:
        continue


    print("Invalid choice, please select 1 or 2.")

print("Game Over.")



