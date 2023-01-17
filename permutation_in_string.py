def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    set_of_characters = list(s1)
    window_size = len(set_of_characters)
    set_of_characters.sort()

    for i in range(len(s2) - window_size + 1):
            new_set = list(s2[i:i + window_size])
            new_set.sort()
            if new_set == set_of_characters:
                    return True
    
    return False


s1 = 'ab'
s2 = 'daaba'
result = checkInclusion(s1, s2)
print(result)

