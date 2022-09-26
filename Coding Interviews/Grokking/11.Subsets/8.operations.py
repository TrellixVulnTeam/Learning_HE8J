def operations(input):
    res = []
    
    if "+"  not in input and "-" not in input and "*" not in input:
        res.append(input)

    else: 
        for i in range(len(input)):
            char = input[i]
            if not char.isdigit():
                leftParts = operations(input[0: i])
                rightParts = operations(input[i+1:])
            
                for left in leftParts:
                    for right in rightParts:
                        if char =="+":
                            res.append(left + right)
                        elif char =="-":
                            res.append(left - right)
                        elif char =="*":
                            res.append(left * right)
    return res
    