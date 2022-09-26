from collections import OrderedDict
input = [
    "00:00,B,1,5.6","00:06,A,1,5.6", "00:05,A,1,5.6", "00:00,A,1,5.6", "00:02,A,1,5.6",
    "00:03,A,2,5.6", "00:04,A,1,5.6", 
]

timeTable = {}
inputArrayTuples = []
for line in input:
    arr = line.split(",")
    inputArrayTuples.append(tuple(arr))

inputArrayTuples = sorted(inputArrayTuples)

currentTime = inputArrayTuples[0][0]
tempDict = OrderedDict()

res = []
for time, ticker, quantity, price in inputArrayTuples:
    
    quantity = int(quantity)
    price = float(price)

    if time != currentTime:
        temp_arr = [currentTime]
        for key, data in tempDict.items():
            temp_arr.append(key)
            temp_arr.append(str(data[0]))
            temp_arr.append(str(data[1]))
        temp_str =",".join(temp_arr)
        res.append(temp_str)
        currentTime = time


    if ticker not in tempDict:
        tempDict[ticker] = (0,0)
    prevQuantity, prevNominal = tempDict[ticker]
    tempDict[ticker] = (prevQuantity + quantity, prevNominal + quantity*price)


        
  
#do it another time
temp_arr = [currentTime]
for ticker, data in tempDict.items():
    temp_arr.append(ticker)
    temp_arr.append(str(data[0]))
    temp_arr.append(str(data[1]))
temp_str =",".join(temp_arr)
res.append(temp_str)
currentTime = time

print(res)
