def return_sorted_list(lst):
    """Given list of sorted lists of integers, 
    return one sorted list containing all the values"""

    n_lists = len(lst)

    if lst == []:
        return []

    to_remove = []
    sorted_list = []

    for n in range(n_lists):
        if lst[n] == []:
            to_remove.append(n)

    for item in to_remove:
        lst.pop(item)
        n_lists -= 1

    while lst:
        if lst[0] == []:
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
            lst.pop(min[1])
            n_lists -= 1

        print(lst)

    return sorted_list

# TO DO: Do merge sort on just 2 lists, then merge with next... (better runtime)


