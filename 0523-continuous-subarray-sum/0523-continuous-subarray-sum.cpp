class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int prefixMod = 0;
        unordered_map<int, int> modSeen;
        modSeen[0] = -1;

        for (int i = 0; i < nums.size(); i++) {
            prefixMod = (prefixMod + nums[i]) % k;

            if (modSeen.find(prefixMod) != modSeen.end()) {
                // ensures that the size of subarray is atleast 2
                if (i - modSeen[prefixMod] > 1) {
                    return 1;
                }
            } else {
                // mark the value of prefixMod with the current index.
                modSeen[prefixMod] = i;
            }
        }

        return 0;
    }
};