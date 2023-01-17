def binary_search(nums: list[int], target: int) -> int:

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
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return -1


def twoSum(numbers, target):
    
    if len(numbers) <= 2:
            return [1, 2]

    for i in range(len(numbers)):
        # if we are searching for 0
        if not target:
            if not numbers[i]:
                return [i + 1, i + 2]

        new_target = target - numbers[i]

        j = binary_search(numbers, new_target)
        if j >= 0:
            if i == j:
                return [i + 1, i + 2]
            return [i + 1, j + 1]

  #     0  1  2  3  4  5  6   7
nums = [1, 2, 3, 4, 4, 9, 56, 90]
nums1 = [-1, -1, 0, 1, 1, 1]
target = -2
result = twoSum(nums1, target)
print(result)