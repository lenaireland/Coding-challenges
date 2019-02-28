# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverse(node):
    prev = None
    current = node

    while current.next is not None:
        ahead = current.next

        current.next = prev
        prev = current
        current = ahead

    current.next = prev

    return current

def addTwoHugeNumbers(a, b):

    """You're given 2 huge integers represented by linked lists. Each linked 
    list element is a number from 0 to 9999 that represents a number with 
    exactly 4 digits. The represented number might have leading zeros. Your 
    task is to add up these huge integers and return the result in the same 
    format.

    Example:
    For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
    addTwoHugeNumbers(a, b) = [9876, 5434, 0].
    Explanation: 987654321999 + 18001 = 987654340000.
    """
    
    a = reverse(a)
    b = reverse(b)
    
    rem = 0
    
    c = None
    
    while a is not None or b is not None:
        if a is None:
            num = b.value + rem
            b = b.next
        elif b is None:
            num = a.value + rem
            a = a.next
        else:
            num = a.value + b.value + rem
            a = a.next
            b = b.next
        
        if num > 9999:
            rem = 1
            num = num - 10000
        else:
            rem = 0
        
        if c is not None:
            next = c
            c = ListNode(num)
            c.next = next
        else:
            c = ListNode(num)
            
    if rem > 0:
        next = c
        c = ListNode(rem)
        c.next = next
        
    return c
        
#         if c is not None:
#             c.next = ListNode(num)
#             c = c.next
#         else:
#             c_head = ListNode(num)
#             c = c_head
        
# #         if a is not None:
# #             a = a.next
# #         if b is not None:
# #             b = b.next

#     if rem > 0:
#         c.next = ListNode(rem)
#         c = c.next
            
#     return reverse(c_head)