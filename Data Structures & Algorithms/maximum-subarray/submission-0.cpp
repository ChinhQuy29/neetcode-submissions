class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum= nums[0];
        int curSum= 0;
        for (int num : nums) {
            curSum= max(curSum, 0) + num;
            maxSum= max(curSum, maxSum);
        }
        return maxSum;
    }
};
