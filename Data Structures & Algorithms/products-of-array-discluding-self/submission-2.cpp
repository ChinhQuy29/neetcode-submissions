class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product= 1;
        int zeroCount= 0;
        for (int num : nums) {
            if (num != 0) {
                product *= num;
            } else {
                zeroCount++;
            }
        }

        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            if (zeroCount) {
                if (zeroCount >= 2) {
                    vector<int> res(nums.size(), 0);
                    return res;
                } else {
                    if (nums[i] == 0) {
                        result.push_back(product);
                    } else {
                        result.push_back(0);
                    }
                }
            } else {
                result.push_back(product / nums[i]);
            }
        }

        return result;
    }
};
