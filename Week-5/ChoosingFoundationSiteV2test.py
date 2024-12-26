# Week-5/ChoosingFoundationSite.py
# -------------------------
# This program gives correct answer
# -------------------------
# 
#
# Week-5/ChoosingFoundationSite.py
# -------------------------
# This program gives correct answer
# -------------------------
# 
#
import math
init = []
init = input().split() #輸入
townNum = int(init[0]) #城市數 n
baseNum = int(init[1]) #基地台數 p
d = int(init[2])     #可涵蓋半徑 d
#print(townNum,baseNum,d)
'''
2≤n≤1000
2≤p≤n
−100≤x ≤100
−100≤y ≤100
1≤Pi ≤100
不會有兩個城鎮落在同一個地點。
'''
if townNum < 2 or townNum > 1000:
 print('n number error')
if baseNum < 2 or baseNum > townNum :
 print('p number error')

dst = []
unvisited = []
hasBuilt = []
covered = []
  
for i in range(townNum):
 dst.append(input().split())
 unvisited.append(i)        #初始化未蓋城市
 for j in range(3):
  if dst[i][j] is None:
   print('None pointer error in town :'+str(i))
  dst[i][j] = int(dst[i][j])
  if int(dst[i][0]) > 100 or int(dst[i][0]) < -100 :#範圍確認
   print('x number error in town :'+str(i))
  if int(dst[i][1]) > 100 or int(dst[i][1]) < -100 :
   print('y number error in town :'+str(i))
  if int(dst[i][2]) > 100 or int(dst[i][2]) < 1 :
   print('people number error in town :'+str(i))
 
for i in range(townNum):
 for j in range(townNum):
  if i==j:
   continue
  if dst[i][0] == dst[j][0] and dst[i][1] ==dst[j][1]:#座標重複確認
   print('two town have same coordinate ERROR')
#print(dst)
'''
dst[0][0] : town 1.x
dst[0][1] : town 1.y
dst[0][2] : town 1.population
dst[7][0] : town 8.x
'''
# find the first base to build
maxppl = -1
firstBase = -1
ppln = 0
cvrppl = 0 #總涵蓋人口
for i in range(townNum):
 if dst[i] is None:
  print('None pointer error in town :'+str(i))
  ppln = dst[i][2]
 for j in range(townNum):
  if i==j: 
   continue
  if dst[j] is None:
   print('None pointer error in town :'+str(j))
  if math.sqrt(pow((dst[i][0]-dst[j][0]),2)+pow((dst[i][1]-dst[j][1]),2)) <= d:
   ppln += dst[j][2]
 
 if ppln > maxppl:
  maxppl = ppln
  firstBase = i

#print(firstBase,maxppl)
hasBuilt.append(firstBase) #已建造
covered.append(firstBase)   #涵蓋範圍
unvisited.remove(firstBase)#尚未建造
cvrppl = maxppl          #可被涵蓋之居民總數
#point first covered    #第一選址後涵蓋區域
for i in unvisited:
 if dst[i] is None:
  print('None pointer error in town :'+str(i))
 if math.sqrt(pow((dst[i][0]-dst[firstBase][0]),2)+pow((dst[i][1]-dst[firstBase][1]),2)) <= d:
  covered.append(i)

#print('covered'+str(covered))
#find next base to build



for k in range(baseNum-1):
 ppln = 0
 maxppl = -1
 nextBase = -1
 for i in unvisited:    #在尚未蓋基地的城市中
  if i not in covered:   #若該城市不在目前可涵蓋範圍內
   ppln = dst[i][2]   #可新增人口數定為該城市人口數
  else:
   ppln = 0     #若該城市已在涵蓋範圍內，則並無新增涵蓋人口
  for j in range(townNum):
   if i==j:
    continue
   if dst[j] is None:
    print('None pointer error in town :'+str(j))
   if math.sqrt(pow((dst[i][0]-dst[j][0]),2)+pow((dst[i][1]-dst[j][1]),2)) <= d:
    if j not in covered: #若 j 城市 與  j 城市 距離小於半徑   d ，且 j 尚未列入涵蓋區域
     ppln += dst[j][2]#可新增人口加入 j 城市之人口
  if ppln > maxppl:
   maxppl = ppln
   nextBase = i    #更新可新增人口數最多之城市
   
  hasBuilt.append(nextBase)
 
 for i in unvisited:
  if dst[i] is None:
   print('None pointer error in town :'+str(i))
  if math.sqrt(pow((dst[i][0]-dst[nextBase][0]),2)+pow((dst[i][1]-dst[nextBase][1]),2)) <= d:
   cvrppl += dst[i][2]#更新可涵蓋總人口
   covered.append(i) #更新covered
 unvisited.remove(nextBase) 

#print('covered'+str(covered))
for i in range(baseNum):
 print(hasBuilt[i]+1, end=' ')
 print(cvrppl)




# 8 1 6 105 (answer given in the question)
# 15 14 7 372 (incorrect, why)
# 6 5 3 190
# 4 14 6 190
# 11 5 3 15 197
# 58 53 23 1652 (incorrect, why)