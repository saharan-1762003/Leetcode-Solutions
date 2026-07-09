#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;

        for(int i = 0; i < nums.size(); i++) {
            int t = nums[i];

            for(int j = i + 1; j < nums.size(); j++) {
                int rem = target - t;

                if(nums[j] == rem) {
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }

        return ans;
    }
};