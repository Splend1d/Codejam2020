import sys
#import time
def comp(s):
   return ''.join(str(1 - int(c)) for c in s)

def findop(ori, new,c):
   #sys.stderr.write(ori+" "+new+"\n")
   if ori[:2] == new:
      sys.stderr.write("no change"+str(c)+"\n")
      return 0 # no change
   elif ori[:2] == comp(new):
      sys.stderr.write("comp"+str(c)+"\n")
      return 1 # comp
   elif ori[2:][::-1] == new:
      sys.stderr.write("inv"+str(c)+"\n")
      return 2 # inv
   else:
      sys.stderr.write("inv + comp"+"\n")
      return 3 # inv + comp
T,B = [int(x) for x in input().split()]

for case in range(T):
   sf = ""
   sb = ""
   #init
   for i in range(5):
      #sys.stderr.write("guess" + str(i+1)+"\n")
      print(i+1)
      sf += input()
   
   for i in range(5):
      #sys.stderr.write("guess" + str(B-i)+"\n")
      print(B-i)
      sb += input()
   anchor = []
   anchor_v = "" 
   for i in range(len(sf)-1):
      tot = int(sf[i])+int(sf[i+1])+int(sb[i])+int(sb[i+1])
      if tot == 1 or tot == 3:
         anchor = [i,i+1]
         anchor_v = sf[i]+sf[i+1]+sb[i+1]+sb[i]
         break
   if len(anchor) == 0:
      anchor = [0] # operation is comp
      anchor_v = sf[0]
   # if bf == bb[::-1]: # inverse = self # if bit != lastbit, op = comp == comp inv != inv == no change
   # elif bf == comp(bb[::-1]): # inverse = comp # if bit != lastbit, op = comp == inv != comp inv == no change
   # op = comp == comp inv != inv never happens  
   count = 0
   while len(sb) + len(sf) < B:
      count += 10
      #sys.stderr.write(sb+" "+sf+" "+" anchor "+" ".join((str(s) for s in anchor))+"\n")
      if len(anchor) == 2:
         newseries = ""
         #sys.stderr.write("guess" + str(anchor[0]+1)+"\n")
         #time.sleep(0.2)
         print(anchor[0]+1)
         #time.sleep(0.2)
         newseries += input()
         #sys.stderr.write("guess" + str(anchor[1]+1)+"\n")
         print(anchor[1]+1)
         newseries += input()
         op = findop(sf[anchor[0]]+sf[anchor[0]+1]+sb[anchor[0]+1]+sb[anchor[0]],newseries,count)
         #sys.stderr.write("before change"+sb+" "+sf+"\n")
         if op == 0:
            pass
         elif op == 1:
            sf = comp(sf)
            sb = comp(sb)
         elif op == 2:
            temp = sf
            sf = sb
            sb = temp
         elif op == 3:
            sf = comp(sf)
            sb = comp(sb)
            #sys.stderr.write("middle change"+sb+" "+sf+"\n")
            temp = sf
            sf = sb
            sb = temp
            
         #sys.stderr.write("after change"+sb+" "+sf+"\n")
      elif len(anchor) == 1:
         #sys.stderr.write("guess" + str(anchor[0]+1)+"\n")
         print(anchor[0]+1)
         newseries = input()
         if sf[anchor[0]] != newseries:
            #sys.stderr.write("comp"+str(count)+"\n")
            sf = comp(sf)
            sb = comp(sb)
         else:
            #sys.stderr.write("nochange"+str(count)+"\n")
            pass
      nowl = len(sf)
      for i in range(4):
         print(nowl+i+1)
         #sys.stderr.write("guess" + str(nowl+i+1)+"\n")
         sf += input()
      
      for i in range(4):
         print(B-i-nowl)
         #sys.stderr.write("guess" + str(B-i-nowl)+"\n")
         sb += input()
      if len(anchor) == 1:
         print(1)
         #sys.stderr.write("guess 1"+ "\n")
         waste = input()
      if len(anchor) == 1:
         for i in range(len(sf)-1):
            tot = int(sf[i])+int(sf[i+1])+int(sb[i+1])+int(sb[i])
            if tot == 1 or tot == 3:
               anchor = [i,i+1]
               #anchor_v = sf[i]+sf[i+1]+sb[i+1]+sb[i]
      #else:
         #anchor_v = sf[i]+sf[i+1]+sb[i+1]+sb[i]
   #sys.stderr.write(sf[:B//2]+sb[::-1][-B//2:]+"\n")
   #time.sleep(0.2)
   print(sf[:B//2]+sb[::-1][-B//2:])
   res = input()
   #sys.stderr.write(res+"\n")
   if res == "N":
      sys.exit(0)

# python 4_interactive_runner.py python 4_testing_tool.py 0 -- python 4.py