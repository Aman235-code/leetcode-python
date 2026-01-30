class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
      def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return current.val


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next



# create first linked list: 2 -> 4 -> 3
l1 = ListNode(2, ListNode(4, ListNode(3)))

# create second linked list: 5 -> 6 -> 4
l2 = ListNode(5, ListNode(6, ListNode(4)))

# print("Linked List 1:")
# print_list(l1)

# print("Linked List 2:")
# print_list(l2)

obj = Solution()
result = obj.addTwoNumbers(l1, l2)
print(result)

# print("Result:")
# print_list(result)
