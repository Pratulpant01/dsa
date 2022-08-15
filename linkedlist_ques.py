# Given the head of a singly linked list, reverse the list, and return the reversed list.


class Solution:
    def reverseList(self):
        curr = self.head
        prev = None
        while curr !=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.


class Solution:
    def hasCycle(self) -> bool:
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode()
    #     tail = dummy
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             tail.next = list1
    #             list1 = list1.next
    #         else:
    #             tail.next = list2
    #             list2 = list2.next
    #         tail= tail.next
    #     if list1:
    #         tail.next = list1
    #     elif list2:
    #         tail.next = list2
    #     return dummy.next
        
