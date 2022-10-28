def check_valid_palindrome(sentence: str) -> bool:
    left, right = 0, len(sentence) - 1

    while left < right:
        while left < right and not ascii_helper(sentence[left]):
            left += 1
        while right > left and not ascii_helper(sentence[right]):
            right -= 1
        if sentence[left].lower() != sentence[right].lower():
            return False
        left += 1
        right -= 1

    return True


def ascii_helper(character: str) -> bool:
    return ord('0') <= ord(character) <= ord('9') or \
           ord('a') <= ord(character) <= ord('z') or \
           ord('A') <= ord(character) <= ord('Z')


if __name__ == '__main__':
    input_string = "A man, a plan, a canal: Panama"
    # input_string = "String efe gnirtS"
    input_string = '-121'
    print(check_valid_palindrome(input_string))
