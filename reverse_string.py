def reverseString(s: list[str]):
    element = s[0]
    s[:] = s[-1:0:-1]
    s.insert(len(s), element)
    
    return None

s = ['e','v','a','c','u','a','t','i','o','n']
print(f'initial: {s}')
s1 = reverseString(s)
print(f'result: {s1}')
print(f'result: {s}')
