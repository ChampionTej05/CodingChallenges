class ValidateSubsequence():
    def __init__(self, nums, seq):
        self.nums = nums
        self.seq = seq

    def validate_subsequence_two_ptr(self):
        numLength = len(self.nums)
        seqLength = len(self.seq)
        if numLength < seqLength:
            return False
        if numLength == 0 or seqLength == 0:
            return False
        if numLength == 1:
            if self.nums[0] == self.seq[0]:
                return True
            return False

        if numLength == seqLength:
            if self.nums[0] != self.seq[0]:
                return False

        numPtr = 0
        seqPtr = 0
        print(numLength, seqLength)
        print(self.nums, self.seq)
        #  order of conditon matter as OR doesn't evaluate second part if first is true
        while (seqPtr < seqLength and numPtr < numLength):
            print("NumPtr , seqPtr", numPtr, seqPtr)
            if self.nums[numPtr] == self.seq[seqPtr]:
                seqPtr += 1
            numPtr += 1

        if seqPtr == seqLength:
            return True
        return False


if __name__ == '__main__':

    nums = [5, 1, 22, 25, 6, -1, 8, 10]
    seq = [1, 6, -1, 10]

    validateSubsequence = ValidateSubsequence(nums, seq)
    result = validateSubsequence.validate_subsequence_two_ptr()
    print(result)
