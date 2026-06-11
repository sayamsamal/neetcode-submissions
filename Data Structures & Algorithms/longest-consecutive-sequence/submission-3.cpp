class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());

        int max_length = 0;

        for (int num : numSet) {
            if (numSet.find(num - 1) != numSet.end()) {
                continue;
            }

            int length = 1;
            while (numSet.find(num + length) != numSet.end()) {
                length++;
            }

            max_length = max(max_length, length);
        }

        return max_length;
    }
};
