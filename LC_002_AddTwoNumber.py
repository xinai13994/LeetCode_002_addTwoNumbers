# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(nodeStart):
    print(nodeStart.val)
    if nodeStart.next == None:
        return
    else:
        printList(nodeStart.next)

class Solution():
    def addTwoNumbers(self, l1, l2):

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        sval = l1.val + l2.val
        if sval < 10:
            ansNode = ListNode(sval)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        else:
            rval = l1.val + l2.val-10
            ansNode = ListNode(rval)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansNode


lst1 = ListNode(2)
sec1 = ListNode(4)
thd1 = ListNode(3)

lst1.next = sec1
sec1.next = thd1

lst2 = ListNode(5)
sec2 = ListNode(6)
thd2 = ListNode(4)

lst2.next = sec2
sec2.next = thd2

ans = Solution()
printList(ans.addTwoNumbers(l1=lst1, l2=lst2))
