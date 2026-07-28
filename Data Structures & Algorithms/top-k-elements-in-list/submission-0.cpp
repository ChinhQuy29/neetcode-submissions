class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> frequency_map;
        for (int number : nums) {
            frequency_map[number]++;
        }
        
        vector<pair<int, int>> arr;
        for (const auto& p : frequency_map) {
            arr.push_back({p.second, p.first});
        }
        sort(arr.rbegin(), arr.rend());
        vector<int> result;
        for (int i= 0; i < k; ++i) {
            result.push_back(arr[i].second);
        }
        return result;
    }
};
