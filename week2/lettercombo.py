lass Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
    
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Start with an empty string in our results queue
        queue = [""]
        
        for digit in digits:
            next_queue = []
            for combination in queue:
                for letter in phone_map[digit]:
                    next_queue.append(combination + letter)
            queue = next_queue
            
        return queue
    
