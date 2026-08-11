class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
          
            if curr.left:
             
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
               
                rightmost.right = curr.right
                
               
                curr.right = curr.left
                curr.left = None
                
           
            curr = curr.right
        
