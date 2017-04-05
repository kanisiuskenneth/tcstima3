from __future__ import print_function
import copy
try:
	import Queue
except:
	print("Please use Python2")

INF = float("inf")

def isInPath(name,path):
	ret = -1
	for i in range(0,len(path)):
		if(name==path[i]):
			ret = i
			break
	return ret
def genCost(adj,path):
	cx = 0
	for i in range(0,len(path)):
		cx += adj[path[i]-1][path[(i+1)%len(path)]-1]
	return cx
def getCost(adj,bname):
	sumx = 0
	for i in range(0,len(adj)):
		cx = 0
		idx = isInPath(i+1,bname)
		x = adj[i][:]
		if(idx == -1):
			x.sort()
			cx += x[0] + x[1]
		elif(idx == 0):
			y = bname[1]
			min = INF
			for j in range(0,len(adj)):
				if(adj[i][j] < min and j!=y-1):
					min = adj[i][j]
			cx+= min + adj[i][y-1]
		elif(idx == len(bname)-1):
			y = bname[len(bname)-2]
			curr = INF
			for j in range(0,len(adj)):
				if(adj[i][j] < min and j!=y-1):
					min = adj[i][j]
			cx+= min + adj[i][y-1]
		else:
			y = bname[idx-1]
			z = bname[idx+1]
			cx+=(adj[i][y-1])+(adj[i][z-1])
		sumx+=cx
	return sumx/2
def genNode(root):
	bname = root[1]
	adj = root[2]
	i = bname[len(bname)-1]
	ret = []
	for j in range(0,len(adj)):
		if(adj[i-1][j] != INF and isInPath(j+1,bname) == -1 ):
			ret.append((getCost(adj,bname+[j+1]),bname + [j+1],adj))
	return ret
	
def findSol(cost,path,adj,count):
	
	ret = genNode((cost,path,adj))
	if(len(adj)-len(path)==1):
		mini = (INF,[],0)
		for i in ret:
			if(i[0] < mini[0]):
				mini = i
		return (mini[0],mini[1],count)
	else:
		q = Queue.PriorityQueue()
		for x in ret:
			count[0]+=1
			q.put((x[0],count[0],x[1],x[2]))
		ctemp = (INF,[],0)
		costnow = INF
		while(not q.empty()):
			temp = q.get()
			if(temp[0] <= costnow):
				ret = findSol(temp[0],temp[2],temp[3],count)
				costnow = genCost(adj,ret[1])
				if(costnow <= ctemp[0]):
					ctemp = ret
					
		return ctemp
				
def startBNB (root):
	count = [1] 
	ret = findSol(0,[1],root,count)
	cost = genCost(root,ret[1])
	path = ret[1]
	count = count[0]
	return (cost,path,count)
