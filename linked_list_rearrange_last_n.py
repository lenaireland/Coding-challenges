# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):

    """Note: Try to solve this task in O(list size) time using O(1) additional 
    space, since this is what you'll be asked during an interview.

    Given a singly linked list of integers l and a non-negative integer n, move 
    the last n list nodes to the beginning of the linked list.

    Examples:
    For l = [1, 2, 3, 4, 5] and n = 3, the output should be
    rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
    For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
    rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6]."""

    if n == 0 or l == []:
        return l
    
    head = l
    current = l
    n_ahead = l
    
    for i in range(n):
        if n_ahead.next == None:
            return l
        n_ahead = n_ahead.next
    
    while n_ahead.next is not None:
        n_ahead = n_ahead.next
        current = current.next
        
    n_ahead.next = head    
    
    start = current.next
    current.next = None
    
    return start