MAX_CHARACTERS = 128  # Please, dont use magic or hardcoded numbers!


def main():
    print(is_unique())
    print(is_unique_without_extra_structure())

def is_unique():
    # Is much easy to test if I define text like a variable
    text = "ABCDEFGHIJKLMNOPQRSTUVWABCABCABC"

    # How many characters? I'm going to assume that there are only 128 characters
    # So, if "text" have more than 128 characters... we can say that string has not all unique characters

    if text.__len__() > MAX_CHARACTERS:
        return False

    letter_state = list(False for _ in range(MAX_CHARACTERS))  # Type: List[bool]

    # Dont use poor variable names
    for letter in text:
        if not letter_state[ord(letter)]:
            letter_state[ord(letter)] = True
        else:
            return False

    return True


def is_unique_without_extra_structure():
    # I'm going to assume that there are only 26 characters (A-Z)
    text = "ABCDEFGA"

    # We have a 26 bits space to save the status
    letter_state = 0b00000000000000000000000000

    for letter in text:
        shift = ord(letter) - ord("A")

        value = letter_state >> shift & 1

        if value == 0:
            mask = 1 << shift
            letter_state = letter_state | mask

        else:
            return False

    return True


if __name__ == '__main__':
    main()
