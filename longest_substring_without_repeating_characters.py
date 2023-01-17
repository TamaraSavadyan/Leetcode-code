def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        set_of_characters = set(s)
        if len(set_of_characters) == 1:
                return 1
        
        window_size = len(set_of_characters)
        while window_size > 1:

                for i in range(len(s) - window_size + 1):
                        new_set = set(s[i:i + window_size])
                        if len(new_set) == window_size:
                                return window_size

                window_size -= 1

        return 0



s = 'abcabcaaa'
s1 = 'aadabac'
length = lengthOfLongestSubstring(s1)
print(length)

s2 = 'aaabbbbab'
setty = set(s2)
# print(setty)

# print(s1[3:9])