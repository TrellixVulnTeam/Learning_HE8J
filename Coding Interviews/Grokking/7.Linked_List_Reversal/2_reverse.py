from common import *
def reverse(head):
    previous, current, next = None, head, None
    while current is not None:
        next = current.next #store next temporarily
        current.next = previous #udate next to previous
        previous = current # set previous to current node 
        current = next # move to next node
    return previous #the last previous will be the head

def main():
    head = list_maker([2,4,6,8,12])
    new_head = reverse(head)
    print_ll(new_head)

main()