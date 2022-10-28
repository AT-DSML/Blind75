from collections import defaultdict


def group_anagrams(list_words: list[str]) -> list[list[str]]:
    dictionary_anagram = defaultdict(list)
    for words in list_words:
        count_array = [0] * 26
        for character in words:
            count_array[ord(character) - 97] += 1
        dictionary_anagram[tuple(count_array)].append(words)
    return list(dictionary_anagram.values())


if __name__ == '__main__':
    input_list = ["ab", "ab", "cs", "op"]
    print(group_anagrams(input_list))
