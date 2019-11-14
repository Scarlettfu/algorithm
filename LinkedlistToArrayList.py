class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def toArrayList(self,head):
        array = []
        while head:
            array.append(head.val)
            head = head.next

        return array


#test#

ledList = ListNode(1)
ledList.next = ListNode(2)
test = Solution()
y = test.toArrayList(ledList)
print (y)

