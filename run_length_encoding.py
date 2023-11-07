def runLengthEncoding(string):

    result = []
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return "1" + string[0]
    currentCounter = 1
    currentCharacter = string[0]
    for idx in range(1, len(string)):
        if string[idx] == currentCharacter:

            if currentCounter == 9:
                result.append(str(currentCounter) + currentCharacter)
                currentCounter = 0
            currentCounter += 1
        else:
            #end of run length
            # store and move forward
            result.append(str(currentCounter) + currentCharacter)
            currentCounter = 1
            currentCharacter = string[idx]
    result.append(str(currentCounter) + currentCharacter)
    return "".join(result)


string = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(string))