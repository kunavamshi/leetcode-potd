class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        vector<pair<int,int>>v;
        v.push_back({nums[0],nums[0]});
        for(int i = 1 ; i < nums.size() ;i++)
        {
            int cur = __builtin_popcount(nums[i]);
            int prev = __builtin_popcount(nums[i-1]);
            if(cur != prev)
            {   
                v.push_back({nums[i],nums[i]});
            }
            v.back().first = min(v.back().first,nums[i]);
            v.back().second = max(v.back().second,nums[i]);
        }
        for(int i = 1 ; i < v.size() ; i++)
        {
            if(v[i-1].second > v[i].first)
                return false;
        }
        return true;
    }
};