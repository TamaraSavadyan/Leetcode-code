def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    slow = 0
    fast  = 2
    if len(nums) - 1 <= fast:
        fast = len(nums) - 1
    number_of_zeros = 0
    if len(nums) == 1:
        return
    while (slow != fast):
        if nums[fast] == 0:
            nums.pop(fast)
            fast -= 1
            number_of_zeros += 1

        if nums[slow] == 0:
            nums.pop(slow)
            fast -= 1
            slow -= 1
            number_of_zeros += 1 

        if fast + 2 <= len(nums) - 1:
            fast += 2
        if slow + 1 <= len(nums) - 1:
            slow += 1   
    
    zeros = [0 for i in range(number_of_zeros)]
    nums += zeros
    # for _ in range(number_of_zeros):
    #     nums.append(0)


# nums = [1, 0, 34, 6, 0, 0, 78, 0, 9]
nums = [1, 0, 0, 1]
print(nums)
moveZeroes(nums) 
print(nums)

# a = 0
# b = 1
# if 0 in {a, b}:
#     print('done')