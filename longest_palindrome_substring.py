class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def expand_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return right - left - 1
        
        
        if len(s) < 1:
            return ""
        
        start = 0
        end = 0
        i = 0
        
        for i in range(len(s)):
            len1 = expand_center(s, i, i)
            len2 = expand_center(s, i, i+1)
            
            length = max(len1, len2)
            
            if length > end - start:
                start = int((i - (length - 1) / 2) + 0.5)
                end = int(i + length / 2)
                
        return s[start:end + 1]        
        
        
#         def isPalindrome(s):
            
#             for i in range(int(len(s)/2)):
#                 if s[i] != s[len(s)-i-1]:
#                     return False
                
#             return True
        
#         to_check = [s]
        
#         while to_check:
#             current = to_check.pop(0)
#             if isPalindrome(current):
#                 return current
#             to_check.append(current[1:])
#             to_check.append(current[:-1])