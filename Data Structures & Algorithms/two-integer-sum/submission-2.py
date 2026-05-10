class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointer solution
        vp = []
        for i in range(len(nums)):
            vp.append([nums[i], i])
        
        vp.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            sum = vp[i][0] + vp[j][0]
            if sum == target:
                return [min(vp[i][1], vp[j][1]), max(vp[i][1], vp[j][1])]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return []