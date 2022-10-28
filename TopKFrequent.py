def main(number_list: list[int], top_k: int) -> list[int]:
    count_bucket = [[] for _ in range(len(number_list) + 1)]
    count_dict = {}
    op = []

    for number in number_list:
        count_dict[number] = count_dict.get(number, 0) + 1

    for num, count in count_dict.items():
        count_bucket[count].append(num)

    max_count = max(count_dict.values())
    min_count = min(count_dict.values())

    for count_index in range(max_count, min_count - 1, -1):
        for number_ in count_bucket[count_index]:
            if len(op) == top_k:
                return op
            op.append(number_)

    return op


if __name__ == '__main__':
    inputList = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8]
    top_k_freq = 2
    print(main(number_list=inputList, top_k=top_k_freq))
