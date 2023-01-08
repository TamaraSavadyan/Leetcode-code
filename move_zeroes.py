def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    j = 0
     
    for i in range(len(nums)):
        
        if nums[i]!= 0 and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]

        if nums[j]!= 0:
            j += 1


# nums = [1, 0, 34, 6, 0, 0, 78, 0, 9]
nums = [1, 0]
print(nums)
moveZeroes(nums) 
print(nums)

