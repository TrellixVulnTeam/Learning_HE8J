#given head, of the linkedlist, find middle node
#if it is even, return the second middle node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_of_linked_list(head):
    slow, fast = head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next
    return slow

def list_maker(arr):
    head = Node(arr[0])
    temp_pointer = head
    for i in range(1, len(arr)):
        temp_pointer.next = Node(arr[i])
        temp_pointer = temp_pointer.next
    return head



# arr = [1,2,3,4,5,6]
# head = list_maker(arr)
# temppointer = head
# print(temppointer.value)
# i = 1
# while i < 6:
#     print(temppointer.next.value)
#     temppointer = temppointer.next
#     i += 1
