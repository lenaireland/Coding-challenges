def lateRide(n):

    """For n = 240, the output should be
    lateRide(n) = 4.

    Since 240 minutes have passed, the current time is 04:00. 
    The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

    For n = 808, the output should be lateRide(n) = 14.

    808 minutes mean that it's 13:28 now, so the answer should be 
    1 + 3 + 2 + 8 = 14"""

    def explicit_ans(n):
        """explicit way"""

        hours = str(n // 60)
        minutes = str(n % 60)
        
        sum = 0
        
        for num in hours:
            sum += int(num)
            
        for num in minutes:
            sum += int(num)
            
        return sum

    def map_function(n):
        """using map function"""

        return sum(map(int, str(n // 60 * 100 + n % 60)))

    def map_fun_explicit(n):
        """Using map function, with more steps"""

        time = (n // 60 * 100 + n % 60)
        print(time)
        
        # use map(function, iterable) to do function to each item in the iterable.
        # returns a map object that can be passed to things like, list or sum to use.
        out = map(int, str(time))

        # if uncomment this next line, consumes map object and can't then sum it 
        # in following return statement
        # print(list(out))
        
        return sum(out)

    # return explicit_ans(n)
    return map_function(n)
    # return map_fun_explicit(n)