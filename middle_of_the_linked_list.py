# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

def middleNode(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        low = 0
        high = len(head)-1
        target = math.ceil((head[low] + head[high]) / 2)
        if head[low] == target:
            return low
        elif head[high] == target:
            return high
        else:
            while (low <= high):
                mid = (low + high)//2
                
                if head[mid] == target:
                    return head[mid:]

                elif head[mid] > target:
                    high = mid - 1

                elif head[mid] < target:
                    low = mid + 1

            return head


print(int((3+4)/2))