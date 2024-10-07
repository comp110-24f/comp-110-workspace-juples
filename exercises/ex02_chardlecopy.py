"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730511752"


def input_word() -> str:
    """func created to take user input word"""
    len_check: int = 5
    guess = str(input("Enter a 5-Character word: "))
    guess_check = len(guess)
    if guess_check == len_check:
        return guess
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return guess


def input_letter() -> str:
    """func created to take user input character"""
    let_len: int = 1
    let_guess = str(input("Enter a single character: "))
    let_check = len(let_guess)
    if let_check == let_len:
        return let_guess
    else:
        print("Error: Character must be a single character.")
        exit()
        return let_guess


def contains_char(word: str, letter: str) -> None:
    """func created to check if letter is in word"""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        index += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        index += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        index += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        index += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        index += 1
    if index == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(index) + " instances of " + letter + " in " + word)
    """final if statements to print if no instances are found"""


def main() -> None:
    """final main func defined"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
