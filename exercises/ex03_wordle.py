"""EX03 - Wordle - Word game"""

__author__ = "730511752"


def input_guess(secret_word_len: int) -> str:
    """This function checks the length of the secert word"""
    "in hindsight I think i made this function wonky"
    index = 0
    while index < 1:
        guess = input(f"Enter a {secret_word_len} character word: ")
        len_guess = len(guess)

        while True:
            if len_guess != secret_word_len:
                guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
                len_guess = len(guess)
            else:
                index += 1
                break

    return guess


def contains_char(selectword: str, selectletter: str) -> bool:
    """this function and loop checks if a word has a certain letter"""
    assert len(selectletter) == 1
    index = 0
    length = len(selectword)
    while index < length:
        check = selectword[index]
        if check == selectletter:
            return True

        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    length = len(guess)
    game_track: str = ""
    """confused on how to create game_track variable to track my emojis"""
    while index < length:
        if guess[index] == secret[index]:
            game_track += GREEN_BOX
            index += 1
        else:
            if contains_char(selectword=secret, selectletter=guess[index]) is True:
                game_track += YELLOW_BOX
                index += 1
            else:
                game_track += WHITE_BOX
                index += 1
    return game_track


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    game_counter = 0
    win = str("\U0001F7E9" * len(secret))
    gameend = str("\U0001F7E8" * len(secret))

    while game_counter < 6 and gameend != win:
        game_counter += 1
        print(f"=== Turn {game_counter}/6 ===")
        gamecheck = input_guess(len(secret))
        gameend = emojified(guess=gamecheck, secret=secret)
        print(gameend)

    if gameend == win:
        print(f"You won in {game_counter}/6 turns!")

    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
