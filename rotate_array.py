def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    return nums[-k:] + nums[:-k]
    # nums.pop(k)
    # for _ in range(k):

    #     nums.insert(0, nums[-1])
    #     nums.pop(-1)
    
    # return nums


nums = [1,2,3,4,5,6,7] #[1, 7, 99, 0, -23, 6]
k = 2
print('initial: ', nums)
print('after rotation: ', rotate(nums, k))
print('rotated: ', nums[-k:])