import numpy as np
def gen(n,mode):
	m = []
	base = [i+1 for i in range(n)]
	if mode == 0:
		for i in range(n):
			m.append(base)
			base = [base[-1]] + base[:-1]
		return m
	elif mode == 2:
		for i in range(n):
			m.append(base)
			base = [base[-1]] + base[:-1]
		m.append(m.pop(-2))
		return m
	elif mode == 1:
		m = [[0]*n for i in range(n)]
		for i in range(n-3):
			m[i] = base
			base = [base[-1]] + base[:-1]
		m[n-3][0] = 2
		m[n-2][-2] = 2
		m[n-1][-1] = 2
		m[n-3][-3] = 1
		m[n-2][-1] = 1
		m[n-1][-2] = 1
		m[n-3][-1] = 3
		m[n-3][-2] = n
		m[n-2][0] = 3
		m[n-1][0] = 4
		#m[n-2][-3] = n-1
		#m[n-1][-3] = n
		#base2 = [3,4,5]
		base2 = [i+3 for i in range(1,n-3)]
		for c in range(1,n-3):
			m[n-3][c] = base2[c-1]
		base3 = [3,min(5,n)]
		mod2 = 1
		for c in range(1,n-2):
			for j in range(2):
				m[n-2+(mod2+j)%2][c] = base3[j]
			mod2 += 1 % 2
			base3 = [min(b+1,n) for b in base3]
		mod3 = 2

		# for c in range(1,n-3):
		# 	for j in range(3):
		# 		m[n-3+(mod3+j)%3][c] = base2[j]
		# 	mod3 += 2 % 3
		# 	base2 = [b+1 for b in base2]
		# if n in m[n-2]:
		# 	m[n-2][n-3] = n-1 
		# 	m[n-1][n-3] = n 
		# else:
		# 	m[n-2][n-3] = n 
		# 	m[n-1][n-3] = n -1
		return m

def p(s):
	print(s)
def decompose(t,n):
	#print("decompose",t,"into",n)
	if n == 3 and t not in [3,6,9]:
		return []
	if t < n or t > n* n:
		return []
	if t == n:
		return [1]*n
	elif t == n*n:
		return [n]*n
	elif t == n+1:
		return []
	elif t == n*n-1:
		return []
	else:
		for i in range(max(1,t//n-1),n+1):
			for j in range(1,n+1):
				if j == i:
					continue
				for k in range(1,n+1):
					if k == i:
						continue
					if i *(n-2) + j + k == trace:
						return [i]*(n-2) + [j,k]
	
	#print("ERROR")
	return []
T = int(input())
for case in range(T):
	n,trace = [int(x) for x in input().split()]
	traces = decompose(trace,n)
	#print("decompose result",traces)
	if len(traces):
		s = set(traces)
	else:
		s = set()
	if len(s) == 1:
		
		ret = gen(n,0)
		map_ = {ret[0][0]:traces[0]}
		#p("type aaaaa")
	elif len(s) == 0:
		print("Case #"+str(case+1)+": IMPOSSIBLE")
		continue
	elif len(s) == 2:
		ret = gen(n,1)
		map_ = {}
		if ret[0][0] != traces[0]:
			map_[ret[0][0]] = traces[0]
		if ret[-1][-1] != traces[-1]:
			map_[ret[-1][-1]] = traces[-1]
		#p("type aaabb")
	else:
		ret = gen(n,2)
		map_ = {ret[0][0]:traces[0],ret[-2][-2]:traces[-2],ret[-1][-1]:traces[-1]}
	swap = set()
	swap.update(list(map_.keys()))
	swap.update(list(map_.values()))
	ks = []
	vs = []
	for s in swap:
		if s not in map_.keys():
			ks.append(s)
		if s not in map_.values():
			vs.append(s)
	assert len(ks) == len(vs)
	for i in range(len(ks)):
		map_[ks[i]] = vs[i] 


	#print(map_)

	print("Case #"+str(case+1)+": POSSIBLE")

		#p("type aaabc")
	for i in range(n):
		for j in range(n):
			if ret[i][j] in map_:
				ret[i][j] = map_[ret[i][j]]
	for r in ret:
		print(" ".join([str(e) for e in r]))