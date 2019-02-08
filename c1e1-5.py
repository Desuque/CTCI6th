
def main():
    print(one_away("ABCD", "ABD"))
    print(one_away("bbcd", "bcd"))
    print(one_away("ABCD", "ABFG"))


def one_away(string_1, string_2):
    if string_1.__len__() + 1 == string_2.__len__():
        return added_char(string_2, string_1)

    if string_1.__len__() - 1 == string_2.__len__():
        return added_char(string_1, string_2)

    if string_1.__len__() == string_2.__len__():
        return replaced_char(string_1, string_2)

    return False


def replaced_char(string_1, string_2):
    iterator = 0
    is_replaced = False
    while iterator < string_1.__len__():
        if string_1[iterator] != string_2[iterator]:
            if is_replaced:
                return False
            is_replaced = True
        iterator += 1
    return True


# string_2 must be bigger than string_1


def added_char(string_1, string_2):
    index_1 = 0
    index_2 = 0

    while index_1 < string_1.__len__() & index_2 < string_2.__len__():
        if string_1[index_1] != string_2[index_2]:
            if index_1 != index_2:
                return False
            else:
                index_2 += 1
        else:
            index_1 += 1
            index_2 += 1
    return True


if __name__ == '__main__':
    main()
