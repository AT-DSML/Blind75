def duplicate_check(list_numbers: list[int]) -> bool:

    set_numbers = set()

    for number in list_numbers:
        if number in set_numbers:
            return True
        set_numbers.add(number)

    return False


if __name__ == '__main__':
    input_list = [1, 2, 3, 1, 4, 5, 6]
    print(duplicate_check(input_list))
