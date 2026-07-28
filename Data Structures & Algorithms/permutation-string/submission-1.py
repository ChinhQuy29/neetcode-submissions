class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        occurrences_s1 = {}
        for char in s1:
            occurrences_s1[char] = 1 + occurrences_s1.get(char, 0)

        occurrences_s2 = {}
        for char in s2[:len(s1)]:
            occurrences_s2[char] = 1 + occurrences_s2.get(char, 0)

        if occurrences_s1 == occurrences_s2:
            return True

        for i in range(len(s1), len(s2)):

            new_char = s2[i]

            old_char = s2[i - len(s1)]

            occurrences_s2[new_char] = 1 + occurrences_s2.get(new_char, 0)

            if occurrences_s2[old_char] == 1:
                del occurrences_s2[old_char]
            else:
                occurrences_s2[old_char] -= 1

            if occurrences_s1 == occurrences_s2:
                return True

        return False
