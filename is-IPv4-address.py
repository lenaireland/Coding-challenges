def isIPv4Address(inputString):
    """Given a string, find out if it satisfies the IPv4 address naming rules."""

    nums = inputString.split(".")
    
    if len(nums) != 4:
        return False
    
    for num in nums:
        try:
            if int(num) > 255 or int(num) < 0:
                return False
        except:
            return False
        
    return True