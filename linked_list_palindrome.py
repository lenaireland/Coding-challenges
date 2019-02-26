# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):

    """Note: Try to solve this task in O(n) time using O(1) additional space, 
    where n is the number of elements in l, since this is what you'll be asked 
    to do during an interview.

    Given a singly linked list of integers, determine whether or not it's a 
    palindrome.

    Examples
    For l = [0, 1, 0], the output should be
    isListPalindrome(l) = true;
    For l = [1, 2, 2, 3], the output should be
    isListPalindrome(l) = false."""

#     current = l
    
#     queue = []
    
#     while current is not None:
#         queue.append(current.value)
#         current = current.next
        
#     while len(queue) > 1:
#         if queue.pop() != queue.pop(0):
#             return False
        
#     return True

    if l is None or l.next is None:
        return True

    slow = l
    fast = l
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    current = slow.next
    prev = None
    
    while current.next is not None:
        # store next node
        ahead = current.next
        # change direction of next pointer
        current.next = prev
        # increment prev and current 
        prev = current
        current = ahead
        
    current.next = prev


    # ANSWER WITHOUT PUTTING LIST BACK IN ORDER
        
    while current is not None and l is not None:
        if l.value != current.value:
            return False
        l = l.next
        current = current.next
        
    return True


    # ANSWER WITH PUTTING LIST BACK IN ORDER

    # ans = True
    # prev = None
    # front = l
    
    # while current.next is not None:
    #     if front.value != current.value:
    #         ans = False
        
    #     front = front.next
        
    #     # put list back in order
    #     ahead = current.next
    #     current.next = prev
    #     prev = current
    #     current = ahead        
        
    # current.next = prev
    
    # if front.value != current.value:
    #     ans = False
    
    # # checking - comment out when correct
    # # current = l
    # # while current.next is not None:
    # #     print(current.value)
    # #     current = current.next        
    # # print(current.value)
        
    # return ans