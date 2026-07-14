class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_nums=[str(i) for i in nums]
        str_nums.sort(key=lambda x: x * 9, reverse=True)
        result = "".join(str_nums)
        if result[0] == "0":
            return "0"
            
        return result
