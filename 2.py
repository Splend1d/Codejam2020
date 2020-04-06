import numpy as np
T = int(input())
for case in range(T):
    ss = input()
    ret = ""
    cur = 0
    for s in ss:
        s= int(s)
        if s > cur:
            ret += '(' * (s-cur)
            cur = s
        else:
            ret += ')' * (cur-s)
            cur = s
        ret += str(s)
    ret += ")" * int(ss[-1])
    print("Case #"+str(case+1)+":",ret)
    #print(retf)