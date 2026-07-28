class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s= {}
        dict_t= {}
        for char in s:
            if char in dict_s.keys():
                dict_s.update({char: dict_s.get(char) + 1})
            else: 
                dict_s.update({char: 1})
        for char in t:
            if char in dict_t.keys():
                dict_t.update({char: dict_t.get(char) + 1})
            else: 
                dict_t.update({char: 1})
        return dict_t == dict_s
            