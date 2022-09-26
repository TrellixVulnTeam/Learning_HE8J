def foo(N):
    i = 0
    res = 0
    temp = []
    while i <= N :
        print(res)
        if i%5 == 0 or i%7 == 0:
            temp.append(i)
        res += i
        i += 1
    # print(sum(temp))
    return res

print(foo(27))