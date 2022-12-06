
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
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                print('more')
                high = mid - 1
            elif nums[mid] < target:
                print('less')
                low = mid + 1
        return -1

    left = 0
    right = len(nums) - 1
    middle = (left + right)//2
    print('middle: ', middle)

    if target == nums[left]:
        return left

    elif target == nums[right]:
        return right

    elif target == nums[middle]:
        return middle

    elif target < nums[middle]:
        print('less')
        return binary_search(nums[middle + 1:], target)

    elif target > nums[middle]:
        print('more')
        return binary_search(nums[:middle], target)

    return -1


answer = binary_search([-1, 0, 3, 4, 5, 6, 7], 5)
print(answer)  # 4
