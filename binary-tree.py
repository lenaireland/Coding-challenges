def minimal_binary_tree(lst, current=None):
    """Given list of integers, build binary tree of minimal height"""

    if lst == []:
        return []


    current = lst[int(len(lst)/2)]

    left = lst[:int(len(lst)/2)]

    right = lst[int(len(lst)/2)+1:]

    # print(current)
    # print(left)
    # print(right)

    tree = minimal_binary_tree(left, current) + minimal_binary_tree(right, current)


