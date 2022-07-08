from concurrent.futures import process
import math
import heapq
import time
from turtle import update
class Order:
    def __init__(self, side, orderID, quantity=0, price=math.inf, display_size= math.inf, time=time.time()):
        self.side = side
        self.orderID = orderID
        self.price = price
        self.quantity = quantity
        self.display_size = display_size
        self.time = time
        self.total_quantity = quantity


    def __str__(self):
        if self.display_size == math.inf:
            return(f'{self.side}: {self.quantity}@{self.price}#{self.orderID}')
        else: 
            return(f'{self.side}: {self.quantity}({self.total_quantity})@{self.price}#{self.orderID}')



    # def __lt__(self, other):
    #     if self.side == "B":
    #         if (self.price == other.price):
    #             return self.time > other.time
    #         return self.price < other.price
    #     if self.side == "S":
    #         if (self.price == other.price):
    #             return self.time > other.time
    #         return self.price > other.price
    
    def __lt__(self, other):
        if self.side == "B":
            if (self.price == other.price):
                return self.time < other.time
            return self.price > other.price
        if self.side == "S":
            if (self.price == other.price):
                return self.time < other.time
            return self.price < other.price
    
    def reduceQuantity(self, quantity):
        self.quantity -= quantity
        if (self.display_size != math.inf):
            self.total_quantity -= quantity
        
    
    def replenish(self):
        if (self.display_size != math.inf):
            if self.quantity == 0:
                if self.total_quantity > self.display_size:
                    self.quantity = self.display_size
                else:
                    self.quantity = self.total_quantity

        #reinserted into db (i.e priority changed)
        self.time = time.time()
       
        
    



print("Please enter your orders")
temp = True 
buy_max_heap = []
sell_max_heap = []


class Orderbook:  
    def __init__(self):
        self.buy = []
        self.sell = []
        self.curr_order = None
        self.cancel = set()
        self.updated = {}
    
    def add_order(self, order):
        if order.display_size != math.inf:
            order.quantity = order.display_size
        if order.price != math.inf:
            if order.side == "B":
                heapq.heappush(self.buy, order)
            if order.side =="S":
                heapq.heappush(self.sell, order)
        
            
    
    def match(self, order, type="MOLO"):
        self.curr_order = order
        if order.side == "B":
            opposing_side = self.sell
        
            if len(opposing_side) == 0:
                self.add_order(order)
                return 0 
            
        if order.side == "S":
            opposing_side = self.buy
            if len(opposing_side) == 0:
                self.add_order(order)
                return 0

        val = 0
        temp_removed = []
        while order.quantity > 0:
            
            self.process_order(order)
            if len(opposing_side) == 0:
                break;
                
            if self.check_price_match(order, opposing_side[0]):
                price = opposing_side[0].price
                if (price == math.inf):
                    price = order.price
                
                val +=  price * min(order.quantity, opposing_side[0].quantity)
                if order.quantity <= opposing_side[0].quantity:
                    opposing_side[0].reduceQuantity(order.quantity)
                    order.reduceQuantity(order.quantity)
                    
                else: 
                    order.reduceQuantity(opposing_side[0].quantity)
                    if type == "IOC":
                        heapq.heappop(opposing_side)
                        break
                    temp_removed.append(opposing_side[0])
                    if (opposing_side[0].display_size != math.inf):
                        #add iceberg order to orderbook
                        opposing_side[0].reduceQuantity(opposing_side[0].quantity)

                        opposing_side[0].replenish()
                        temp = opposing_side[0]
                        heapq.heappop(opposing_side)
                        heapq.heappush(opposing_side, temp)
                     
                        if opposing_side[0].total_quantity == 0:
                            heapq.heappop(opposing_side)
                    else:
                        heapq.heappop(opposing_side)
            else:
                break

        if type =="ICE":
            if order.total_quantity > 0:
                order.quantity = order.display_size
                self.add_order(order)
    
            return val

        if type == "FOK":
            if order.quantity > 0:
                for order in temp_removed:
                    self.add_order(order)
                # print("yes")
                return 0
            return val

        if type != "IOC":
            print(order)
            if order.quantity > 0:
                self.add_order(order)
        return val

       

                
    def process_order(self, order):
        orderID = order.orderID
        if orderID in self.cancel:
            if (order.side == "B"):
                if (len(self.buy) > 0):
                    heapq.heappop(self.buy)
            else:
                if (len(self.sell) > 0):
                    heapq.heappop(self.sell)
            self.cancel.remove(order.orderID)
            
        if(orderID in self.updated):
            updated_quantity, updated_price = self.updated[orderID][0], self.updated[orderID][1]
            #price is the same,
            if (updated_price == order.price):
                order.quantity = updated_quantity
                if (updated_quantity > order.quantity):
                    order.time = time.time()

            #price is different
            else:
                order.price = updated_price
                order.quantity = updated_quantity
                order.time = time.time()
        

    def check_price_match(self, order1, order2):
        if (order1.side == "B"):
            buy = order1
            sell = order2
        else:
            buy = order2
            sell = order1

            if (sell.price == math.inf):
                return True

        return buy.price >= sell.price
    
    def cancel_order(self, orderID):
        self.cancel.add(orderID)
        print(self.cancel)
        
    def update_order(self, orderID, quantity, price):
        self.updated[orderID] = (quantity, price)
        
    def print(self):
        i = 0
        while i < len(self.buy):
            # self.process_order(self.buy[0])
            print(self.buy[i], end=",")
            i+=1
        print("||")
        i = 0
        while i <  len(self.sell):
            # self.process_order(self.sell[0])
            print(self.sell[i], end=",")
            i +=1
        print("end")

    # def print(self):
    #     while len(self.buy) > 0:
    #         self.process_order(self.buy[0])
    #         print(heapq.heappop(self.buy), end=",")
    #     print("||")
    #     while len(self.sell) > 0:
    #         self.process_order(self.sell[0])
    #         print(heapq.heappop(self.sell), end=",")
    
    


a = Orderbook()
while True:
    action, orderType, side, orderId, quantity, price = 0,1,2,3,4,5
    inputArr = input().split(' ')
    if inputArr[action] == "END":
        break
    if inputArr[action] == "SUB":
        if inputArr[orderType]  =="LO":
            order = Order(inputArr[side], inputArr[orderId], int(inputArr[quantity]), int(inputArr[price]))
            print(a.match(order))
            a.print()
        elif inputArr[orderType] == "MO":
            order = Order(inputArr[side], inputArr[orderId], int(inputArr[quantity]))
            print(a.match(order))
            a.print()
        elif inputArr[orderType] == "FOK" or inputArr[orderType] == "IOC":
            order = Order(inputArr[side], inputArr[orderId], int(inputArr[quantity]), int(inputArr[price]))
            print(a.match(order, inputArr[orderType]))
            a.print()
        elif inputArr[orderType] =="ICE":
            order = Order(inputArr[side], inputArr[orderId], int(inputArr[quantity]), int(inputArr[price]), int(inputArr[-1]))
            print(a.match(order, inputArr[orderType]))
            a.print()
            

    if inputArr[action] =="CXL":
        a.cancel_order(inputArr[1])
    if inputArr[action] == "CRP":
        a.update_order(inputArr[1], inputArr[2], inputArr[3])

a.print()
