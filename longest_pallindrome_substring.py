# https://www.algoexpert.io/questions/longest-palindromic-substring


def isPallindrome(string):
    return string == string[::-1]


#O(n*n*n) solution
def longestPalindromicSubstring_v1(string):
    # Write your code here.

    maxStringLength = 0
    result = ""
    subSet = ""
    for idx in range(len(string)):
        for endIdx in range(idx, len(string)):
            subSet = string[idx:endIdx + 1]  #get the complete string
            if len(subSet) > maxStringLength and isPallindrome(subSet):
                maxStringLength = len(subSet)
                result = subSet

    print(subSet)
    return result


def getLongestPallindromeIdx(string, startIdx, endIdx):

    while (startIdx >= 0 and endIdx < len(string)):
        if string[startIdx] != string[endIdx]:
            break
        else:
            startIdx -= 1
            endIdx += 1

    # endIdx-1 because either we have breaked out of the current loop because of mismatch of element endIdx is not in pallindrome or we have run out of string length. Same logic goes for startIdx+1
    intervalForPallindrome = (endIdx - 1) - (
        startIdx + 1) + 1  # 1 at last since it is 0 based index
    return [startIdx + 1, endIdx]


def longestPalindromicSubstring(string):

    maxLengthPIdx = [0, 1]  #single length i.e string[0:1]
    # result = string[0]

    for i in range(1, len(string)):
        oddLengthPIdx = getLongestPallindromeIdx(string, i - 1, i + 1)
        eventLengthPIdx = getLongestPallindromeIdx(string, i - 1, i)

        #find which one of the two index list has bigger interval
        currentLengthPIdx = max(oddLengthPIdx,
                                eventLengthPIdx,
                                key=lambda x: x[1] - x[0])
        # find the global longest
        maxLengthPIdx = max(maxLengthPIdx,
                            currentLengthPIdx,
                            key=lambda x: x[1] - x[0])

    return string[maxLengthPIdx[0]:maxLengthPIdx[1]]
