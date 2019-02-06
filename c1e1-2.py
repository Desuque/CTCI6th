def main():
    print(check_permutation("ABAA", "BAAA"))
    print(another_way_to_do_this("AAABCD", "BCDAAA"))
    print(another_way_to_do_this("AAABCD", "BCDAAD"))


def check_permutation(string_1, string_2):
    # Case sensitive? Yes or no?
    # There are spaces? Please, give me some extra info :)
    # We can sort the two strings and compare to find differences, but not today :)

    # Check the length, if different -> false
    if string_1.__len__() != string_2.__len__():
        return False

    string_2_state = list(0 for _ in range(string_2.__len__()))

    for letter_1 in string_1:
        for i, letter_2 in enumerate(string_2, start=0):
            if string_2_state[i] != 1:
                if letter_1 == letter_2 and string_2_state[i] == 0:
                    string_2_state[i] = 1
                    # print(string_2_state)
                    break

    # I dont like the double (triple) for ...
    for state in string_2_state:
        if state == 0:
            return False
    return True


MAX_CHARACTERS = 128


def another_way_to_do_this(string_a, string_b):
    # Imagine the same length

    # I suppose 128 ASCII
    count_of_letters = list(0 for _ in range(MAX_CHARACTERS))

    for letter in string_a:
        count_of_letters[ord(letter)] += 1

    for letter in string_b:
        count_of_letters[ord(letter)] -= 1
        if count_of_letters[ord(letter)] < 0:
            return False
    return True


if __name__ == '__main__':
    main()
