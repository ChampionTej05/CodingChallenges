class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def push(self, number):

        self.stack.append(number)
        if len(self.minStack) == 0 or number <= self.minStack[-1]:
            self.minStack.append(number)
        if len(self.maxStack) == 0 or number >= self.maxStack[-1]:
            self.maxStack.append(number)

    def pop(self):

        answer = -1
        if len(self.stack) > 0:
            answer = self.stack.pop()
            if self.minStack and answer == self.minStack[-1]:
                self.minStack.pop()
            if self.maxStack and answer == self.maxStack[-1]:
                self.maxStack.pop()

        return answer

    def getMin(self):

        if self.minStack:
            return self.minStack[-1]

    def getMax(self):
        if self.maxStack:
            return self.maxStack[-1]


import unittest


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)


obj = TestProgram()
obj.test_case_1()