class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class Solution:
    def ArrayListToLinkedList(self,nums):
        head = p = None
        for num in nums:
            if head is None:
                head = ListNode(num)
                p = head
            else:
                p.next = ListNode(num)
                p = p.next
        return head

list = (1,2,3,4,5)
test = Solution()

result = test.ArrayListToLinkedList(list)
while result:
    print (result.val)
    result = result.next