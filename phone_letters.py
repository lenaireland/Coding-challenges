class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':

        """Given a string containing digits from 2-9 inclusive, return all 
        possible letter combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is 
        given. Note that 1 does not map to any letters."""
        
        dict = {'0': [],
                '1': [], 
                '2': ['a','b','c'],
                '3': ['d','e','f'],
                '4': ['g','h','i'],
                '5': ['j','k','l'],
                '6': ['m','n','o'],
                '7': ['p','q','r','s'],
                '8': ['t','u','v'],
                '9': ['w','x','y','z']}
        
        output = []
        
        for char in digits:
            letters = dict[char]
            
            new_output = []
            
            for letter in letters:
                if output == []:
                    new_output = letters[:]
                for entry in output:
                    new_output.append(entry+letter)
                    
            output = new_output[:]
            
        return output