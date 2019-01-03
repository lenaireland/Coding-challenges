def validTime(time):
    """Check if the given string is a correct time representation of the 
    24-hour clock."""

    split_time = time.split(':')
    
    if len(split_time) != 2:
        return False
    
    if int(split_time[0]) < 0 or int(split_time[0]) > 23:
        return False
    if int(split_time[1]) < 0 or int(split_time[1]) > 59:
        return False
    
    return True