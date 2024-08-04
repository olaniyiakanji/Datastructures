import random

def get_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    tries = 6
    print("Welcome to Hangman!")
    
    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print(f"You have {tries} tries left.")
        print("Used letters: ", ' '.join(used_letters))
        
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print(f"Good guess! '{guess}' is in the word.")
            else:
                tries -= 1
                print(f"Sorry, '{guess}' is not in the word.")
        elif guess in used_letters:
            print("You already guessed that letter. Try again.")
        else:
            print("Invalid input. Please enter a letter.")
        
        print("\n")
    
    if tries == 0:
        print(display_hangman(tries))
        print(f"Game over! The word was '{word}'. Better luck next time!")
    else:
        print(f"Congratulations! You guessed the word '{word}'!")

if __name__ == "__main__":
    play_hangman()
