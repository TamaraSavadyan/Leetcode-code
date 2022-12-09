def sortedSquares(nums):
    
    new_list = [x**2 for x in nums]
    
    return sorted(new_list)