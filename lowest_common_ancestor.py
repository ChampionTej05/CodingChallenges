# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    import sys
    MIN_SIZE = -sys.maxsize

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        p_path = []
        q_path = []
        isPPresent = self.find_node_path(root, p, p_path)
        isQPresent = self.find_node_path(root, q, q_path)
        #safety check
        if not (isPPresent and isQPresent):
            return -1
        common_ancestor = self.find_last_common(p_path, q_path)
        if common_ancestor == self.MIN_SIZE:
            return -1
        return common_ancestor

    def find_node_path(self, root, target, node_path=[]):
        if not root:
            return 0

        temp = root
        # add current node to path
        node_path.append(temp)
        if temp.val == target.val:
            return 1

        # check if it's left and right tree has value
        presentInLeft = self.find_node_path(temp.left, target, node_path)
        print("is Present in Left : ", presentInLeft)
        if presentInLeft:
            return 1
        presentInRight = self.find_node_path(temp.right, target, node_path)
        print("is Present in Right : ", presentInRight)
        if presentInRight:
            return 1

        # Neither current root nor their children has any presence so we are in wrong path. Traverse back

        node_path.pop()
        return 0

    def find_last_common(self, arr, brr):
        '''
        this method finds the last common element between two arrays
        '''

        common_element = self.MIN_SIZE

        k = 0

        while (k < len(arr) and k < len(brr)):
            if arr[k].val == brr[k].val:
                common_element = arr[k]
            k += 1
        return common_element

    def lowestCommonAncestor(self, root, p, q):
        # BaseCase: if root is reached at null return root or if p or q found return that root
        if root == None or root == p or root == q:
            return root

        #After that we move to left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # While coming back if the left node is null return the right one or vice versa
        if left == None:
            return right
        elif right == None:
            return left
        # If above both condition are not true that means we have found that root under which both p and q lies
        else:
            return root


# one more solution for binary Tree using better recursion

# if it is case of binary search tree then ?


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class Solution(object):
    import sys
    MIN_SIZE = -sys.maxsize

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #lowest ancestor is the node in which we have to go on different sides to search the nodes
        # so as long as we are on same node path to reach, we will go down.
        # first node on which we see that we have to go on separate way, will our node

        while (root):
            rootValue = root.val
            if p.val < rootValue and q.val < rootValue:
                root = root.left
            elif p.val > rootValue and q.val > rootValue:
                root = root.right
            else:
                #either p , q are equal to root
                # or we p>r<q or p<r>q
                return root
