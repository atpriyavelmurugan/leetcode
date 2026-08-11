class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l=[]
        
     
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
   
        seen = set()
        
        for i, char in enumerate(s):
         
            if char in seen:
                continue
                
        
            while l and l[-1] > char and last_occurrence[l[-1]] > i:
                removed_char = l.pop()  
                seen.remove(removed_char)  
                
            l.append(char)  
            seen.add(char)  
            
        return "".join(l)

                        
