#given the head, find starting node of cyle
#find length of cycle
'''
1. find length of cyle
2. move pointer 2 ahead to K
3. move both pointers until they meet
4. thats the start
'''

def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        current_length += 1
        if current == slow:
            break
        return cycle_length

def find_starting_node(head, cycle_length):
    pointer1 = head
    pointer2 = head
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    
    while pointer1 != pointer2:
        pointer1 =  pointer1.next
        pointer2 = pointer2.next 
    return pointer1


def find_cycle_start_main(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None: #o(n)
        fast = fast.next.next
        slow = slow.next
        if slow == fast: #found cycle
            cycle_length = calculate_cycle_length(slow) #o(n)
            break
    return find_starting_node(head, cycle_length) #o(n)
    
# total is o(3n) which is o(n)

    