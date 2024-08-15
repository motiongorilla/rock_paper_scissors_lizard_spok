import random

outcomes = {"Rock": ["Scissors", "Lizard"], "Paper": ["Rock", "Spok"], "Scissors": ["Paper", "Lizard"], "Lizard": ["Spok", "Paper"], "Spok": ["Scissors", "Rock"]}
def play_rpsls():
    comp_choice = random.choice(list(outcomes))
    resolve = outcomes[comp_choice]

    pl_choice = str(input("Choose! [R]ock, [P]aper, [S]cissors, [L]izard, Sp[o]k\n")).lower()
    in_var = {"r": "Rock",
            "rock": "Rock",
            "p": "Paper",
            "paper": "Paper",
            "s": "Scissors",
            "scissors": "Scissors",
            "l": "Lizard",
            "lizard": "Lizard",
            "o": "Spok",
            "spok": "Spok"}

    player = in_var[pl_choice].casefold()

    if player == comp_choice.casefold():
        print(f"It's a tie! I chose {comp_choice}")
    else:
        if player in resolve:
            print(f"You lose! I chose {comp_choice}")
        else:
            print(f"You won! I chose {comp_choice}")

    replay = str(input("Want to play again? [y/n]\n")).lower()
    if replay == "y" or replay == "yes":
        play_rpsls()


play_rpsls()