'''
https://leetcode.com/problems/ransom-note/
'''

from collections import Counter


def canConstruct(ransomnote, magazine):
    magazine_ctr = Counter(magazine)
    print("Magazine Counter", magazine_ctr)
    for ele in ransomnote:
        print("ele ", ele)
        if ele not in magazine_ctr:
            return False
        if magazine_ctr[ele] < 1: return False
        magazine_ctr[ele] -= 1
        print("Updated Magazine Ctr ", magazine_ctr)

    return True


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self, ransomnote, magazine, expectedAnswer):
        self.assertEqual(canConstruct(ransomnote, magazine), expectedAnswer)


obj = TestProgram()

ransomnote = "aa"
magazine = "ab"
expectedAnswer = False
obj.test_case_1(ransomnote, magazine, expectedAnswer)
