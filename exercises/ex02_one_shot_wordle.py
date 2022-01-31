"""EX02 - One Step Wordle - We're getting there."""

__author__ = "730472431"

secret: str = "python"

guess: str = str(input(f"What is your {len(secret)}-letter guess: "))

while len(guess) != len(secret):
    guess = str(input(f"That was not {len(secret)} letters. Try again: "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

count: int = 0
emoji: str = ""

while (count < len(secret)):
    if (guess[count] == secret[count]):
        emoji = emoji + GREEN_BOX
    else:
        in_word: int = 0
        is_in_word: bool = False
        while (in_word < len(secret)):
            if (guess[count] == secret[in_word]):
                is_in_word = True
            in_word = in_word + 1
        if not is_in_word:
            emoji = emoji + WHITE_BOX
        else:
            emoji = emoji + YELLOW_BOX
    count = count + 1

print(emoji)

accuracy: int = 0
final_print: str = ""

while ((len(emoji) - 1) > accuracy):
    if (emoji[accuracy] != GREEN_BOX):
        final_print = "Not quite. Play again soon!"
    accuracy += 1

if (final_print != "Not quite. Play again soon!"):
    final_print = "Woo! You got it!"

print(final_print)
