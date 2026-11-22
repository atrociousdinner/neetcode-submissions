# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        fast = head
        slow = head
        pair_sum = 0
        additive = []

        while fast and fast.next:
            additive.append(slow.val)
            fast = fast.next.next
            slow = slow.next


        while slow:
            pair_sum = max(pair_sum, additive[-1] + slow.val)
            additive.pop(-1)
            slow = slow.next

        return pair_sum
        