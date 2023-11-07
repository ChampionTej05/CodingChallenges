def caesarCipherEncryptor(string, key):

    newString = []
    std = 97
    modular = 26
    for item in string:
        value = (ord(item) - std + key) % modular
        value = value + std
        # print("Item , old value, new value ", item, ord(item), value)
        value
        newString.append(chr(value))
    # print(newString)
    return "".join(newString)

'''
Create test for caesarCipherEncryptor
'''
def test_caesarCipherEncryptor():
    input = "xyz"
    key = 2
    assert caesarCipherEncryptor(input, key) == "zab"
    print("Test passed")
input = "xyz"
key = 2
print(caesarCipherEncryptor(input, key))
