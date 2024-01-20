import random
import hangman_details


def replay_func():
    replay = input("\nLet's play again? (Y/N)\n").lower()
    try:
        if replay == "y":
            game_func()
        elif replay == "n":
            print("\nBye Bye")
        else:
            print("Invalid input")
            replay = input("\nLet's play again? (Y/N)\n").lower()
    except ValueError:
        print("Invalid input")


def game_func():

    display = []
    game_word = random.choice(hangman_details.word_list).lower()
    for _ in range(len(game_word)):
        display += "_"
    print(" ".join(display))
    end_game = False
    life = 6
    incorrect_guesses = []

    while not end_game:
        guess = (input("Please enter a letter\n").lower())
        
        if guess.isalpha() is True and len(guess) == 1:
            for position in range(len(game_word)):
                letter = game_word[position]
                if letter == guess:
                    display[position] = letter
            if guess not in game_word:
                print(hangman_details.stages[life])
                life -= 1
                if guess in incorrect_guesses:
                    pass
                else:
                    incorrect_guesses += guess
                if life == 0:
                    print(hangman_details.stages[0])
                    hangman_details.animator2(hangman_details.lost, delay=1, repeat=5)
                    replay_func()
                    break
            print(f"\nincorrect guesses: {' '.join(incorrect_guesses)}\n")
            print(' '.join(display))
            if "_" not in display:
                end_game = True
                print(f"The word is {''.join(display)}\n")
                hangman_details.animator(hangman_details.win, delay=0.1, repeat=10)
                print(f"\n{replay_func()}")
        else:
            print("Invalid input")

game_func()



#try to put the hangman on my website
