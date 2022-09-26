from collections import OrderedDict
input = [
    "00:00,B,1,5.6","00:06,A,1,5.6", "00:05,A,1,5.6", "00:00,A,1,5.6", "00:02,A,1,5.6",
    "00:03,A,2,5.6", "00:04,A,1,5.6", 
]
def printDict(dict, printStatus):
    arr = []
    for ticker, data in dict.items():
        if (ticker in printStatus):
            arr += [ticker, str(data[0]), str(data[1])]
    
    return ",".join(arr)




timeTable = OrderedDict()
inputArrayTuples = []
for line in input:
    arr = line.split(",")
    inputArrayTuples.append(tuple(arr))
inputArrayTuples = sorted(inputArrayTuples)

currentTime = - 100
timeMap = OrderedDict()

for time, ticker, quantity, price in inputArrayTuples:
    quantity, price = int(quantity), float(price)
    if time not in timeMap:
        timeMap[time] = {}
    timeMap[time][ticker] = (quantity, price)


for i in range(0, len(timeMap)):
    
    currTime = list(timeMap.keys())[i]
    arr = [currTime]
    prev = list(timeMap.values())[i-1]
    current = list(timeMap.values())[i]

    if i == 0:
        prev = {}

    for ticker, data in current.items():
        quantity = data[0]
        nominal = data[0] * data[1]
        if ticker in prev:
            prevQuantity, prevNominal = prev[ticker]
            arr += [ticker, quantity+prevQuantity, nominal+prevNominal]
        else: 
            arr+= [ticker, quantity, nominal]
        
        timeMap[currTime][ticker] = (quantity, nominal)
    
    print(arr)