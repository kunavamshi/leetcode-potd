#include <vector>
#include <unordered_map>

class Solution {
public:
    int numSubarraysWithSum(std::vector<int>& nums, int goal) {
        std::unordered_map<int, int> count;
        int sum = 0, result = 0;
        
        for (int num : nums) {
            count[sum]++;
            sum += num;
            result += count[sum - goal];
        }
        
        return result;
    }
};