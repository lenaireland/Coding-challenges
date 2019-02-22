# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):

    """Given a singly linked list of integers l and an integer k, remove all 
    elements from list l that have a value equal to k."""
    
    if l == None:
        return l
    
    try:
        while l.value == k:
            l = l.next          
    except:
        return None
        
    current = l
    
    while current.next is not None:
        if current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
            
    return l