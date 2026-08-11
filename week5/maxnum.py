class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
   
        def get_max_subsequence(nums, length):
            stack = []
            drop = len(nums) - length  
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]

        def merge(sub1, sub2):
            return [max(sub1, sub2).pop(0) for _ in range(len(sub1) + len(sub2))]

        max_result = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end + 1):
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > max_result:
                max_result = candidate
            
        return max_result
