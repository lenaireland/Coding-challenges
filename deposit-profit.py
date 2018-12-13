def depositProfit(deposit, rate, threshold):
    """You have deposited a specific amount of money into your bank account. 
    Each year your balance increases at the same growth rate. With the 
    assumption that you don't make any additional deposits, find out how long 
    it would take for your balance to pass a specific threshold. """

    amt = deposit
    i = 0
    
    while amt < threshold:
        i += 1
        amt = amt*(1+rate/100)
        
    return i