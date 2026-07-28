class Solution {
public:
    bool isPalindrome(string s) {
        string new_s= "";
    for (char letter: s) {
        if ((int(letter) >= 97 && int(letter) <= 122) || (int(letter) >= 48 && int(letter) <= 57)) {
            new_s += letter;
        } else if ((int(letter) >= 65 && int(letter) <= 90)) {
            new_s += char(int(letter) + 32);
        }
    }

    string reversed_s= "";
    for (int i= new_s.length() - 1; i >= 0; i--) {
        reversed_s += new_s[i];
    }
        if (new_s != reversed_s) {
            return false;
        }
        return true;
    }
};
