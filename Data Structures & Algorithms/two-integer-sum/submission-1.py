class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map solution
        map = {}

        # 1. Iterate through the list
        # 2. Calculate diff,
        #   if diff not in map -> Add {num, idx} to map
        #   if diff in list -> Return [map{diff}, i]
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
