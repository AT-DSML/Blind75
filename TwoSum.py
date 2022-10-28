def two_sum(number_list: list[int], num: int) -> tuple[int]:
    bag_number = {}

    for index in range(len(number_list)):
        if num - number_list[index] in bag_number:
            return bag_number[num - number_list[index]], index + 1
        bag_number[number_list[index]] = index + 1
    return ()


if __name__ == '__main__':
    input_list = [1, 1, 3, 4, 5, 4]
    number = 5
    print(two_sum(input_list, number))
