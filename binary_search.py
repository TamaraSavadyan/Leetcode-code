class Solution:
    def search(self, nums: list[int], target: int) -> int:

        middle = len(nums)//2

        if target == nums[middle]:
            return middle

        elif target <= nums[middle]:
            return self.search(nums[:middle + 1], target)

        elif target >= nums[middle]:
            return self.search(nums[middle - 1:], target)

        return -1




binary_search = Solution()

answer = binary_search.search([-1, 0, 1, 2, 3, 4, 5, 6, 7], 5)
print(answer)