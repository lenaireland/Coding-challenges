def isMAC48Address(inputString):
    """A media access control address (MAC address) is a unique identifier 
    assigned to network interfaces for communications on the physical network 
    segment.

    The standard (IEEE 802) format for printing MAC-48 addresses in 
    human-friendly form is six groups of two hexadecimal digits (0 to 9 or 
    A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

    Your task is to check by given string inputString whether it corresponds 
    to MAC-48 address or not."""

    # without regex
    
    # hexadecimals = set(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])

    # hexdecs = inputString.split('-')
    
    # if len(hexdecs) != 6:
    #     return False
    
    # for hexdec in hexdecs:
    #     if len(hexdec) != 2:
    #         return False
    #     for char in hexdec:
    #         if char not in hexadecimals:
    #             return False
            
    # return True

    # with regex
    import re
    return re.search(r"^([0-9A-F]{2}-){5}[0-9A-F]{2}$", inputString) is not None