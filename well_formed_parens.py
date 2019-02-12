class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':

        """Given n pairs of parentheses, write a function to generate all 
        combinations of well-formed parentheses.

        For example, given n = 3, a solution set is:

        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
        """
        
        ans = []
        
        def add_parens(expr, left, right):
            
            if len(expr) == 2*n:
                ans.append(expr)
                return
            if left < n:
                add_parens(expr + "(", left + 1, right)
            if right < left:
                add_parens(expr + ")", left, right + 1)
                
        add_parens("", 0, 0)
        
        return ans