def gibonacci(n, x, y):
    if n == 0:
        return x
    if n == 1:
        return y
    return gibonacci(n - 1, x, y) - gibonacci(n - 2, x, y)


def gibonacci_iterative(n, x, y):
    gibArray = [x, y]
    #edge case 1
    if n == 0:
        return gibArray[0]
    #edge case 2
    if n == 1:
        return gibArray[1]
    # print("GibArray at the start:", gibArray)
    for i in range(2, n + 1):
        # print(i)
        gibArray.append(gibArray[i - 1] - gibArray[i - 2])
        # print("GibArray", gibArray)
    # print("last gibarray", gibArray)
    return gibArray[n]


def gib(n, x, y):
    if n == 0:
        return x
    if n == 1:
        return y
    temp_1 = x
    temp_2 = y
    for i in range(2, n + 1):
        temp = temp_2 - temp_1
        temp_1 = temp_2
        temp_2 = temp
    return temp_2


import unittest


class TestProgram(unittest.TestCase):

    func = None

    def test_case_n_0(self):
        print("test1")
        n = 0
        x = 1
        y = 2
        expected = 1
        actual = self.func(n, x, y)
        self.assertEqual(expected, actual)

    def test_case_n_1(self):
        print("test2")
        n = 1
        x = 1
        y = 2
        expected = 2
        actual = self.func(n, x, y)
        self.assertEqual(expected, actual)

    def test_case_n_2(self):
        print("test3")
        n = 2
        x = 1
        y = 2
        expected = 1  # there is mistake in test plan for this case, it should be 1 not -1
        actual = self.func(n, x, y)
        print("actual 3", actual)
        self.assertEqual(expected, actual)

    def test_case_n_5(self):
        print("test4")
        n = 5
        x = 2
        y = 4
        expected = -2
        actual = self.func(n, x, y)
        print("actual 4", actual)

        self.assertEqual(expected, actual)

    def test_case_n_10_5(self):
        print("test4")
        n = 10**5
        x = 65
        y = 13
        expected = -13
        actual = self.func(n, x, y)
        print("actual 4", actual)

        self.assertEqual(expected, actual)

    def test_case_n_10_7(self):
        print("test4")
        n = 10**7 + 1
        x = 65
        y = 13
        expected = 52
        actual = self.func(n, x, y)
        print("actual 4", actual)

        self.assertEqual(expected, actual)

    def test_case_run(self, gib):
        self.func = gib
        print("Running test cases against Gibonacci")
        self.test_case_n_0()
        self.test_case_n_1()
        self.test_case_n_2()
        self.test_case_n_5()
        self.test_case_n_10_5()
        self.test_case_n_10_7()


obj = TestProgram()
obj.test_case_run(gib)