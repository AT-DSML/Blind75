def product_except_self(number_list: list[int]) -> list[int]:
    op = [1] * len(number_list)

    imaginary = 1
    for index in range(len(number_list)):
        op[index] *= imaginary
        imaginary *= number_list[index]
    imaginary = 1
    for index in range(len(number_list)-1, -1, -1):
        op[index] *= imaginary
        imaginary *= number_list[index]

    return op


if __name__ == '__main__':
    input_list = [1, 2, 3, 5, 3]
    print(product_except_self(input_list))
