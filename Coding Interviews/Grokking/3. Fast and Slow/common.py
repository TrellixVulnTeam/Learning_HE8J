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

def print_ll(head):
    temp_pointer = head
    while temp_pointer is not None:
        print(temp_pointer.value)
        temp_pointer = temp_pointer.next
        if temp_pointer == None:
            break


        