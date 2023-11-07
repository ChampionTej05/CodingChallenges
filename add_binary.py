'''
Sum of two binary strings 
https://leetcode.com/problems/add-binary/
'''


def addBinary(a, b):
    a_int, b_int = int(a, 2), int(b, 2)
    sum_int = a_int + b_int
    return bin(sum_int).replace('0b', '')


def binaryToDecimal(bin_str):
    '''
    Without using any built in functions 
    '''

    sum_int = 0
    counter = 0
    for ch in reversed(bin_str):
        if ch == '1':
            temp = pow(2, counter)
            sum_int += temp
        counter += 1

    return sum_int


def decimalToBinary(dec_num):
    '''
    Divide Number by 2 
    Store the remainder
    Divide the Quotient by 2 till quotient = 0
    '''
    remainders = []
    if dec_num == 0:
        return "0"
    while (dec_num > 0):
        remainder = dec_num % 2
        remainders.append(remainder)
        dec_num = dec_num // 2

    return "".join([str(ch) for ch in remainders[::-1]])


def addBinaryWithoutBuiltIn(a, b):
    a_int, b_int = binaryToDecimal(a), binaryToDecimal(b)
    sum_int = a_int + b_int

    return decimalToBinary(sum_int)


a, b = "0", "0"
print(addBinaryWithoutBuiltIn(a, b))

# bin_str = "1011"
# print(binaryToDecimal(bin_str))

# dec_num = 11
# print(decimalToBinary(dec_num))