# 1. Fast and Slow

For this pattern we basically follow a very simple idea.
If there is a **cycle** in the linkedlist, we will surely find them using the fast and slow pointers (they will meet)

```py
# to initialise a node we do this
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# to make a list
def list_maker(arr):
    head = Node(arr[0])
    temp_pointer = head
    for i in range(1, len(arr)):
        temp_pointer.next = Node(arr[i])
        temp_pointer = temp_pointer.next
    return head

# basic idea of finding a cycle
def find_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if (fast == slow):
            return True
    return False

```

## 1.1. Linked list cycle

## 1.2. Start of cycle

## 1.3. Happy Number

## 1.4. Middle of linkedlist
