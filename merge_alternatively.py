class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        for s in zip(word1, word2):
            result += s[0] + s[1]

        w1_len = len(word1)
        w2_len = len(word2)

        if w1_len > w2_len:
            result += word1[w2_len:]
        elif w2_len > w1_len:
            result += word2[w1_len:]

        return result


s = Solution()
res = s.mergeAlternately('apeaaa', 'plbnn')
print(res)
