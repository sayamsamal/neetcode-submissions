class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(), nums.end());
        int count = 0;
        int maxCount = 0;
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] == nums[i-1] + 1) {
                count++;
            } else if (nums[i] == nums[i-1]) {
                continue;
            } else {
                count = 0;
            }
            if (count > maxCount) maxCount = count;
        }
        return maxCount + 1;
    }
};
