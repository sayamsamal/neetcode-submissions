class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        vector<int> prefP(n);
        vector<int> sufP(n);

        prefP[0] = 1;
        sufP[n-1] = 1;

        // Prefix Product
        for (int i = 1; i < n; i++) {
            prefP[i] = nums[i-1] * prefP[i-1];
        }

        // Suffix Product
        for (int i = n-2; i >=0; i--) {
            sufP[i] = nums[i+1] * sufP[i+1];
        }

        for (int i = 0; i < n; i++) {
            res[i] = prefP[i] * sufP[i];
        }

        return res;
    }
};
