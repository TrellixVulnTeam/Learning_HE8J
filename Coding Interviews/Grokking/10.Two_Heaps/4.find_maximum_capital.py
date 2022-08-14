from heapq import heappop, heappush
from typing import final

#lets say we don't have any projects to buy, our final capital will just be initial Plus whatever profit
def find_maximum_capital(numOfProjects, initialCapital, profits, capitals):
    profitHeap = [] #for profit
    capitalHeap = [] #for capital
    available_capital = initialCapital

    #insert all the capital into minheap
    for i in range(len(capitals)):
        heappush(capitalHeap, (capitals[i], i))
    
    #for maximum amount of projects
    for _ in range(numOfProjects):
        #get all the projects that are within our ability
    
        while capitalHeap and capitalHeap[0][0] <= available_capital:
            capital, index = heappop(capitalHeap)
            heappush(profitHeap, (-profits[index], index))
        
        #if profit heap is empty -> break (means no capital)
        if not profitHeap:
            break

        available_capital += -heappop(profitHeap)[0]
    
    return available_capital

print(find_maximum_capital(2,1,[1,2,3], [0,1,2]))
        

