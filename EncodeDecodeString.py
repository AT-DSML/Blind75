class Solution:
    @staticmethod
    def encode_string(string_list: list[str]) -> str:
        encoded_string = ''
        for word in string_list:
            if word is None:
                continue
            encoded_string += str(len(word)) + '#' + word
        return encoded_string

    @staticmethod
    def decode_string(encoded_string: str) -> list[str]:
        result, index = [], 0
        while index < len(encoded_string):
            temp = index
            while encoded_string[temp] != '#':
                temp += 1
            result.append(encoded_string[temp + 1:temp + 1 + int(encoded_string[temp - 1])])
            index = temp + int(encoded_string[temp - 1]) + 1
        return result


if __name__ == '__main__':
    sol = Solution()
    input_list = ["leet", "code", None, "you"]
    encoded = sol.encode_string(input_list)
    print(encoded)
    print(sol.decode_string(encoded))
