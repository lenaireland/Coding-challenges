class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without 
        repeating characters.
        
        :type s: str
        :rtype: int
        """
        
        dict = {}
        long_len = 0
        
        for i in range(len(s)):
            if s[i] in dict:
                new_len = len(dict)
                if new_len > long_len:
                    long_len = new_len
                old_index = dict[s[i]]
                new_dict = {}
                for key, value in dict.items():
                    if value > old_index:
                        new_dict[key] = value
                dict = new_dict.copy()
                dict[s[i]] = i
            else:
                dict[s[i]] = i
        
        new_len = len(dict)
        if new_len > long_len:
            long_len = new_len
            
        return long_len