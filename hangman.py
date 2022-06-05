import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = '-' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []

    lives = 6

    print("Let's play Hangman!")
    print(display_hangman(lives))
    print('You have used these letters: ', ' '.join(guessed_letters))
    print('Current word: ', ' '.join(word_completion))
    print('\n')   
    
    while not guessed and lives > 0:

        guess = input('Please guess a letter or word: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the character", guess)
            
            elif guess not in word:
                print(guess, 'is not in the word.')
                lives = lives - 1
                guessed_letters.append(guess)
            
            else:
                print(f'Good job! {guess} is in the word.')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if '-' not in word_completion:
                    guessed = True
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You have already guessed the word', guess)
            
            elif guess != word:
                print(guess, 'is not the word.')
                lives = lives - 1
                guessed_words.append(guess)
            
            else:
                guessed = True
                word_completion = word
        
        else:
            print("This is not a valid guess. Please try again.")
        
        print(display_hangman(lives))
        print('You have used these letters: ', ' '.join(guessed_letters))
        print('Current word: ', ' '.join(word_completion))
        print('\n')

    
    if guessed:
        print(f'Congratulations! You have guessed the word {word} correctly!')
    else:
        print(f'Sorry, you ran out of lives. The correct word was {word}.')



def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                    ---------
                    |/      |
                    |       O
                    |      \|/
                    |       |
                    |      / \
                   ---
                """,
                # head, torso, both arms, and one leg
                """
                    ---------
                    |/      |
                    |       O
                    |      \|/
                    |       |
                    |      / 
                   ---
                """,
                # head, torso, and both arms
                """
                    ---------
                    |/      |
                    |       O
                    |      \|/
                    |       |
                    |      
                   ---
                """,
                # head, torso, and one arm
                """
                    ----------
                    |/       |
                    |        O
                    |       \|
                    |        |
                    |     
                   ---
                """,
                # head and torso
                """
                    ---------
                    |/      |
                    |       O
                    |       |
                    |       |
                    |     
                   ---
                """,
                # head
                """
                    ---------
                    |/      |
                    |       O
                    |    
                    |      
                    |     
                   ---
                """,
                # initial empty state
                """
                    ---------
                    |/      |
                    |      
                    |    
                    |      
                    |     
                   ---
                """
    ]
    return stages[lives]


def main():
    word = get_word()
    play(word)
    while input('Play again? (Y/N)').upper == 'Y':
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()