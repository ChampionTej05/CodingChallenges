'''
Approach :
Traverse the string with 2-ptr. Start and end. Start : Substring Start, end : Substring end with no-duplicate
For each chr in String at pointer END
1. Check if it exists in mapper 
    - if not, add it to mapper with count and increment END value
    - if yes, save the string till now [start, end-1]. 
        - remove the count of all values of substring [start, end-1] from mapper
        till the value of END index
        ex: clement , so in this if we encounter second 'e', remove all values till first 'e' 
        i.e (c,l,e)
'''

def longestSubstringWithoutDuplication(string):
    # Write your code here.
    mapper = {}

    start = 0 
    end = 0 
    lengthOfString = len(string)
    resultSubString = []
    currentSubString = []
    while (end < lengthOfString):
        chr = string[end]
        if chr not in mapper:
            mapper[chr] = 1 
            currentSubString.append(chr)
        else:
            # remove values from start to end till duplicate character 
            duplicateChar = chr 
            while ( start<end):
                
                mapper.pop(string[start])
                start+=1
                if string[start-1]==duplicateChar:
                    break

            # save the string 
            if len(currentSubString) > len(resultSubString):
                resultSubString = currentSubString
                
            # we removed values till duplicate character in the above while loop
            currentSubString = list(string[start:end+1])
            mapper[duplicateChar] = 1

        print(mapper, start, end, currentSubString, string[end])
        end+=1
        

    if len(currentSubString) > len(resultSubString):
                resultSubString = currentSubString
    print(resultSubString)
    return ''.join(resultSubString)
    

# write test case for longestSubstringWithoutDuplication

def test_longestSubstringWithoutDuplication():
    string = 'clementisacap'
    assert longestSubstringWithoutDuplication(string) == 'mentisac'
    print("Test passed")


# string = 'abcdeabcdefc'
# print(longestSubstringWithoutDuplication(string))