def return_sorted_list(lst):
    """Given list of sorted lists of integers, 
    return one sorted list containing all the values"""

    n_lists = len(lst)

    if lst == []:
        return []

    sorted_list = []

    while lst:
        while lst[0] == []:
            lst.pop(0)
            n_lists -= 1

        min = [lst[0][0], 0]
        # print(min)

        for n in range(n_lists):
            print(n)
            print(n_lists)
            if lst[n][0] < min[0]:
                min = [lst[n][0], n]

        sorted_list.append(lst[min[1]].pop(0))
        print(sorted_list)

        if lst[min[1]] == []:
            n_lists -= 1

        # print(n_lists)

    return sorted_list


