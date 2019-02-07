class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        """Write a function to find the longest common prefix string amongst an 
        array of strings.

        If there is no common prefix, return an empty string "".
        """
        
        common = ''
        
        if strs == []:
            return common
        
        minimum = min(map(lambda x: len(x),strs))
            
        for j in range(minimum):
            letter = ''
            for i in range(len(strs)):
                if letter == '':
                    letter = strs[i][j]
                else:
                    if letter != strs[i][j]:
                        return common
            common += letter
            
        return common