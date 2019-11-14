class listNode(object):

    def __init__(self, val, next = None):

        self.val = val
        self.next = next

class Solution:
    def findNodeinLinkedList(self, head, val):
        if not head:
            return None
        while head:
            if head.val == val:
                return head
            else:
                head = head.next

        return None

linkedList = listNode(0, None)
test = Solution()
print (test.findNodeinLinkedList(linkedList,1))
