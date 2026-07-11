class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberMap = { 
            '2': 'abc', 
            '3': 'def',
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv', 
            '9': 'wxyz'
        }
        if not digits: 
            return []
        output = ['']
        for digit in digits: 
            new = []
            for temp in output: 
                for c in numberMap[digit]:
                    new.append(temp + c)
            output = new
        
        return output


