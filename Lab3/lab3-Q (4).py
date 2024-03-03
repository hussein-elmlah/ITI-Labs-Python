class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_counter = {}
        max_length = 0
        start_index = 0

        for end_index, char in enumerate(s):
            if char in char_counter and char_counter[char] >= start_index:
                start_index = char_counter[char] + 1
            char_counter[char] = end_index
            max_length = max(max_length, end_index - start_index + 1)

        return max_length
