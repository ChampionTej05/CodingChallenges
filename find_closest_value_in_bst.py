class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, value):
    """Find the closest value in BST. Assumed that there will be only ONE closest value in BST

    Args:
        value (int): Value to search for 
    """

    if tree is None:
        return None

    if tree.value == value:
        return tree.value

    result = tree.value
    if value - tree.value < 0:
        # left side
        temp = findClosestValueInBst(tree.left, value)
        if temp:
            result = temp

    if value - tree.value > 0:
        # right side
        temp = findClosestValueInBst(tree.right, value)
        if temp:
            result = temp

    return result
