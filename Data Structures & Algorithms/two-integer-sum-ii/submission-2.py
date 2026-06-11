class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx2 = len(numbers) - 1
        idx1 = 0
        while idx2 > idx1:
            sum = numbers[idx1] + numbers[idx2]

            if sum > target:
                idx2 -= 1
            elif sum < target:
                idx1 += 1
            else:
                break
        return [idx1+1, idx2+1]

            
