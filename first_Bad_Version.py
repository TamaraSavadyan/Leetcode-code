# def isBadVersion(version):
#     pass
#     # this func checks if version is bad (it was in the exercise)

# def firstBadVersion(n: int) -> int:
#     nums = [i for i in range(n)]
#     print(nums)
#     low = 0
#     high = len(nums)-1
#     if isBadVersion(nums[low]):
#         return nums[low]
#     elif isBadVersion(nums[high]) and not isBadVersion(nums[high - 1]):
#         return nums[high]
#     else:
#         while (low <= high):
#             mid = (low+high)//2
#             if isBadVersion(nums[mid]) and not isBadVersion(nums[mid - 1]):
#                 return nums[mid]
#             elif isBadVersion(nums[mid - 1]):
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return -1

# firstBadVersion(5)


first_bad = 0
def isBadVersion(version):
   if version >= first_bad:
      return True
   return False
class Solution:
   def firstBadVersion(self, n):
      if n <2:
         return n
      start = 1
      end = n
      while(start<=end):
         mid = (start+end)//2
         if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
         elif isBadVersion(mid-1):
            end = mid-1
         else:
            start = mid+1

ob1 = Solution()
first_bad = 1
op = ob1.firstBadVersion(2)
print(op)