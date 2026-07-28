class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in mpp.keys():
                mpp[sorted_string] = [string]
            else:
                mpp[sorted_string].append(string)
            
        return [value for _, value in mpp.items()]