def evenDigitsOnly(n):
    """Check if all digits of the given integer are even."""

    n_str = str(n)
    
    for num in n_str:
        if int(num) % 2 != 0:
            return False
    
    return True