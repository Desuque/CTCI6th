def main():
    print(is_rotation("caramelo", "rameloca"))
    print(is_rotation("bottle", "bolett"))


def is_substring(string1, string2):
    return string2 in string1  # <-- Love python


def is_rotation(string1, string2):
    # Create a new string
    new_string = string1 + string1

    # Its a good idea code something like this
    if string1.__len__() > 0 and string2.__len__() <= string1.__len__():
        return is_substring(new_string, string2)

    return False


if __name__ == '__main__':
    main()