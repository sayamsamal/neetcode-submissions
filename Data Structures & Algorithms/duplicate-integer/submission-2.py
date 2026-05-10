class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hash Set Length
        return len(set(nums)) < len(nums)