def absoluteValuesSumMinimization(a):
    """Given a sorted array of integers a, find an integer x from a such that 
    the value of
    abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
    is the smallest possible (here abs denotes the absolute value).
    If there are several possible answers, output the smallest one."""

    for x_num in a:
        sum = 0
        for num in a:
            sum += abs(num - x_num)
        try:
            if sum < min_sum:
                x = x_num
                min_sum = sum
        except:
            x = x_num
            min_sum = sum
            
    return x