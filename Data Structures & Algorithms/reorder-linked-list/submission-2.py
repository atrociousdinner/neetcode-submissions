# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next

        l = 0
        r = len(values)-1

        new_values = []

        while l <= r:
            new_values.append(values[l])
            l += 1

            if l <= r:
                new_values.append(values[r])
                r -= 1

        curr = head
        i = 0

        while curr:
            curr.val = new_values[i]
            curr = curr.next
            i += 1 


        



        

        