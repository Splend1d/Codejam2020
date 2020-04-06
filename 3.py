import numpy as np
T = int(input())
for case in range(T):
	na = int(input())
	ls = []
	for i in range(na):
		ls.append([int(x) for x in input().split()]+[i])
	ls = sorted(ls)
	j = 0
	c = 0
	ret = [0] * na
	flag = False
	for a in ls:
		if a[0] >= j:
			j = a[1]
			ret[a[2]] = "J"
		elif a[0] >= c:
			c = a[1]
			ret[a[2]] = "C"
		else:
			flag = True
			print("Case #"+str(case+1)+": IMPOSSIBLE")
			break
	if not flag:		
		print("Case #"+str(case+1)+":","".join(ret))