import numpy as np
T = int(input())
for case in range(T):
	sq = int(input())
	ls = []
	for i in range(sq):
		ls.append([int(x) for x in input().split()])
	m = np.matrix(ls)
	trace = 0
	rr = 0
	for n,r in enumerate(m):
		
		rl = r.tolist()[0]
		trace += rl[n]
		s = set()
		s.update(rl)
		if len(s) != len(rl):
			rr += 1
	m = m.transpose()
	cc = 0
	for n,r in enumerate(m):
		rl = r.tolist()[0]
		s = set()
		s.update(rl)
		if len(s) != len(rl):
			cc += 1
	print("Case #"+str(case+1)+":",trace,rr,cc)