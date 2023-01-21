def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    list_of_characters = list(s1)
    window_size = len(list_of_characters)
    list_of_characters.sort()

    for i in range(len(s2) - window_size + 1):
            new_list = list(s2[i:i + window_size])
            new_list.sort()
            if new_list == list_of_characters:
                    return True
    
    return False


s1 = 'ab'
s2 = 'daaba'
result = checkInclusion(s1, s2)
print(result)

