class Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimal_binary_tree(lst):
    """Given list of integers, build binary tree of minimal height"""
        
    if lst == []:
        return None

    if len(lst) == 1:
        return Node(lst[0])



    current = lst[int(len(lst)/2)]

    node = Node(current)

    node.left = minimal_binary_tree(lst[:int(len(lst)/2)])

    node.right = minimal_binary_tree(lst[int(len(lst)/2)+1:])

    # checking
    print("Current is {}".format(current))
    print("Node.data is {}".format(node.data))
    try:
        print("Node.left.data is {}".format(node.left.data))
    except:
        pass
    try:
        print("Node.right.data is {}".format(node.right.data))
    except:
        pass

    return node



