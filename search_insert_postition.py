
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums)-1
    if nums[low] == target:
        return low
    elif nums[high] == target:
        return high
    else:
        while (low <= high):
            mid = (low+high)//2

            if nums[mid] == target:
                
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1

        return low

                     #  0  1  2  3  4  5  6
answer = searchInsert([-1, 0, 2, 4, 5, 6, 7], 3)
print(answer)


