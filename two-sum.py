import time
startTime = time.time()


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        k = 0
        for count, number in enumerate(nums):
            k += 1
            for i in range(k, len(nums)):
                if number + nums[i] == target:
                    return [count, i]
        return None


a = Solution()
result = a.twoSum([3, 2, 4], 6)
print(result)
print((time.time() - startTime)*1000, 'ms')