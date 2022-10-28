def isomorphic_string(w_one: str, w_two: str) -> bool:
    if len(w_one) != len(w_two):
        return False

    word_map = {}

    for index in range(len(w_one)):

        if (w_one[index] in word_map and word_map[w_one[index]] != w_two[index]) \
            or \
           (w_one[index] not in word_map and (w_two[index] in word_map or w_two[index] in word_map.values())):
            return False

        word_map[w_one[index]] = w_two[index]

    return True


if __name__ == '__main__':
    word_one = 'abf'
    word_two = 'pba'
    print(isomorphic_string(word_one, word_two))
