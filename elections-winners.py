def electionsWinners(votes, k):
    """Elections are in progress!

    Given an array of the numbers of votes given to each of the candidates so 
    far, and an integer k equal to the number of voters who haven't cast their 
    vote yet, find the number of candidates who still have a chance to win the 
    election.

    The winner of the election must secure strictly more votes than any other 
    candidate. If two or more candidates receive the same (maximum) number of 
    votes, assume there is no winner at all."""

    leader = max(votes)
    
    possible_winners = 0        
    
    for count in votes:
        if k == 0:
            if count == leader:
                possible_winners += 1
            if possible_winners > 1:
                return 0
        else:
            if count + k > leader:
                possible_winners += 1
            
    return possible_winners