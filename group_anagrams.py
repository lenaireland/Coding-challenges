class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Given an array of strings, group anagrams together.

        Example:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        Note: All inputs will be in lowercase. The order of your output does not 
        matter.
        """
        
        groups = {}
        
        for word in strs:
            # char_list = []
            # for char in word:
            #     char_list.append(char)
                
            # char_list.sort()
            # chars = ''.join(char_list)
            chars = ''.join(sorted(word))
            
            if chars in groups:
                groups[chars].append(word)
            else:
                groups[chars] = [word]
                
        ans = []
                
        for anagrams in groups.values():
            ans.append(anagrams)
                           
        return ans