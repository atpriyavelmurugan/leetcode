class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.stack = list(reversed(nestedList))
    
    def next(self) -> int:
      
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            
            
            self.stack.pop()
            for curr in reversed(top.getList()):
                self.stack.append(curr)
                
        return False
