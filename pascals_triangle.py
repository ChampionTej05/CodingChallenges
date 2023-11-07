'''
Intuition : for middle element, it's value is equal to the value of upper element and upper left element.
matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-1]

steps
1. for every rows, no of cols will be row+1 (row is 0-indexed)
2. keep the end elements 1 for each row 
3. calculate the middle elements 
'''


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Write your code here.
        # Return a list of lists.
        result = []
        # n = int(n)
        for i in range(numRows):
            cols_in_row = i + 1
            alist = [0] * (cols_in_row)

            # make end elements 1
            alist[0] = 1
            alist[i] = 1

            # recur for middle elements till i-1

            for j in range(1, i):
                alist[j] = result[i - 1][j] + result[i - 1][j - 1]

            result.append(alist)

        return result