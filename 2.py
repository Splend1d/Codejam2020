import numpy as np
T = int(input())
for case in range(T):
	ss = input()
	def build(s,lv,cur):
		pos = [-1]
		#print(s,lv,cur)
		if len(s) == 0:
			return ""
		while len(pos) == 1:
			lv += 1
			for p,e in enumerate(s):
				if int(e) == lv:
					pos.append(p)
			

		#print(pos)
		ret = ""
		ft = "("*(lv-cur)
		bk = ")"*(lv-cur)
		ret += ft
		if len(s) == 1:
			return ft + str(lv) + bk
		for i in range(len(pos)-1):
			ret += build(s[pos[i]+1:pos[i+1]],lv,lv)
			ret += str(lv) 
		try:
			ret += build(s[pos[i+1]+1:],lv,lv)
		except:
			pass
		ret += bk
		return ret
	
	ret = build(ss,-1,0)
	#print(ret)
	# retf = ""
	# i = 0
	# while i < len(ret)-1:
	# 	if ret[i] == ")" and ret[i+1] == "(":
	# 		i += 2
	# 		continue
	# 	retf += ret[i]
	# 	i += 1
	# retf += ret[-1]
	print("Case #"+str(case+1)+":",ret)
	#print(retf)