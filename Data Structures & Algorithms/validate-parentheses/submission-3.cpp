class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2) {
            return false;
        }
        stack<char> st;
        map<char, char> mp= {{'{', '}'}, {'[', ']'}, {'(', ')'}};
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            } else {
                if (st.empty()) {
                    return false;
                } else {
                    if (mp[st.top()] != c) {
                        return false;
                    } else {
                        st.pop();
                    }
                }
            }
        }
        return st.empty();
    }
};
