def reverseWords(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    l = s[::-1].split(' ')
    s1 = ' '.join(l[::-1])

    return s1


s = "I'm a GOOD Doctor"
print(f'initial: {s}')
# l = s[::-1].split(' ')
# print(l)
# print(l[::-1])
# s1 = ' '.join(l[::-1])
# print(s1)

print(f'result: {reverseWords(s)}')