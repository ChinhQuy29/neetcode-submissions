class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        set<int> ordered_s;
        for (int num : nums) {
            ordered_s.insert(num);
        }
        int length= 1;
        int maxLength= 1;
        for (auto it= ordered_s.begin(); it != ordered_s.end(); ++it) {
            auto next_it= next(it);
            if ((next_it != ordered_s.end()) && (*it == *next_it - 1)) {
                length++;
            } else {
                if (length > maxLength) {
                    maxLength= length;
                }
                length= 1;
            }
        }
        return maxLength;
    }
};
