def isBadVersion(version):
    pass
    # this func checks if version is bad (it was in the exercise)

def firstBadVersion(n: int) -> int:
    nums = [i for i in range(n)]
    print(nums)
    low = 0
    high = len(nums)-1
    if isBadVersion(nums[low]):
        return low
    elif isBadVersion(nums[high]) and not isBadVersion(nums[high - 1]):
        return high
    else:
        while (low <= high):
            mid = (low+high)//2
            if isBadVersion(nums[mid]) and not isBadVersion(nums[mid - 1]):
                return mid
            elif isBadVersion(nums[mid - 1]):
                high = mid - 1
            else:
                low = mid + 1
        return -1

firstBadVersion(5)