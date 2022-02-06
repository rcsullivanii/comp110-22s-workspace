"""Coding a structured wordle."""

__author__ = "730472431"

secret = "codes"


def contains_char(any_length: str, single_char: str) -> bool:
    """Searches the first spyttring for any instance of the second string, a character."""
    assert len(single_char) == 1
    i: int = 0
    while(len(any_length) > i):
        if(any_length[i] == single_char):
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji which corresponds to whether guess's characters are included/properly placed in secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0
    while(len(secret) > i):
        if(secret[i] == guess[i]):
            emoji += GREEN_BOX
        elif(contains_char(secret, guess[i])):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(length: int) -> str:
    """Prompts the user to enter a length character long word and ensures their response agrees."""
    guess: str = input(f"Enter a {length} character word: ")
    while (len(guess) != length):
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    GREEN_BOX: str = "\U0001F7E9"
    correct_entry: str = len(secret) * GREEN_BOX
    while(len(secret) + 1 >= i):
        print(f"=== Turn {i}/6 ===")
        guess: str = (emojified(input_guess(len(secret)), secret))
        if(guess == correct_entry):
            print(guess)
            print(f"You won in {i}/6 turns!")
            i = i + (len(secret) + 2)
        else:
            print(guess)
            i += 1
        if(i == (len(secret) + 2)):
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()