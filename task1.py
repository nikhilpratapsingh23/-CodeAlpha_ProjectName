import random

def hangman():
    
    words = ["python", "coding", "hangman", "script", "project"]
    
    
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6
    word_display = ["_"] * len(chosen_word)
    
    print(" Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    
    while attempts_left > 0 and "_" in word_display:
        print("\nWord: ", " ".join(word_display))
        print(f"Attempts left: {attempts_left}")
        guess = input("Enter a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet.")
            continue
        
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in chosen_word:
            print(" Correct!")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print("Wrong guess.")
            attempts_left -= 1
    
    if "_" not in word_display:
        print(f"\n You guessed it! The word was '{chosen_word}'.")
    else:
        print(f"\n Game over! The word was '{chosen_word}'.")

if __name__ == "__main__":
    hangman()

