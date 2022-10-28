def longest_consecutive(nums: list[int]) -> int:
    longest = 0
    num_set = set(nums)
    for num in nums:
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == '__main__':
    input_list = [100, 4, 200, 1, 3, 2]
    # input_list = [0, 1, 1, 2]
    # input_list = [0]
    # input_list = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # input_list = [0, -1]
    print(longest_consecutive(input_list))
