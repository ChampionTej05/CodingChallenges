def isPalindrome(input):
    if len(input) == 1:
        return True

    start = 0
    end = len(input) - 1

    while (start <= end):
        if input[start] == input[end]:
            start += 1
            end -= 1
        else:
            return False

    return True


def isPalindromeRecursion(input, start=0):
    end = len(input) - 1 - start
    if start >= end:
        return True
    isCheck = input[start] == input[end] and isPalindromeRecursion(
        input, start + 1)
    return isCheck


input = "abba"
print(isPalindromeRecursion(input))