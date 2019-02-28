# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#     
def reverse_k_nodes(l,k):    
    undo = False
    tail = l
    
    prev = None
    current = l
    
    for i in range(k):
        if current.next is not None:
            ahead = current.next
            current.next = prev
            prev = current
            current = ahead
        elif i == (k-1):
            current.next = prev
            prev = current
            current = None
        else:
            undo = True
            n = i + 1
            current.next = prev
            break
    
    if undo:
        prev = None
        for i in range(n):
            ahead = current.next
            current.next = prev
            prev = current
            current = ahead     

    head = prev
    
    return([head, tail, current])
    

def reverseNodesInKGroups(l, k):

    """Given a linked list l, reverse its nodes k at a time and return the 
    modified list. k is a positive integer that is less than or equal to the 
    length of l. If the number of nodes in the linked list is not a multiple of 
    k, then the nodes that are left out at the end should remain as-is.

    You may not alter the values in the nodes - only the nodes themselves can 
    be changed."""

    head, tail, current = reverse_k_nodes(l,k)
    start = head
    
    while current:
        new_head, new_tail, current = reverse_k_nodes(current, k)
        
        tail.next = new_head
        head = new_head
        tail = new_tail
        
    return start