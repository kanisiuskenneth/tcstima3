from __future__ import print_function
import copy
try:
	import Queue
except:
	print("Please use Python2")
	quit()
import util
INF = float("inf")

#Melakukan Reduksi Matrix terhadap baris
def reduce_by_row(adj):
	n = len(adj)
	lb = 0
	for i in range(0,n):
		min = INF
		for j in range(0,n):
			if (adj[i][j] < min):
				min = adj[i][j];
		for j in range(0,n):
			if(adj[i][j] != INF):
				adj[i][j] = adj[i][j]-min 
		if(min != INF):
			lb+=min
	return lb

#Melakukan reduksi Matrix terhadap kolom
def reduce_by_col(adj):
	n = len(adj)
	lb =0
	for i in range(0,n):
		min = INF
		for j in range(0,n):
			if(adj[j][i] < min):
				min = adj[j][i]
		for j in range(0,n):
			if(adj[j][i] != INF):
				adj[j][i] = adj[j][i]-min 
		if(min != INF):
			lb+=min
	return lb

#Melakukan Reduksi Matrix total
def reduce_all(adj):
	lb =0;
	lb += reduce_by_row(adj)
	lb += reduce_by_col(adj)
	return lb
	
def select(x,i,j):
	adj = copy.deepcopy(x)
	n = len(adj)
	for a in range(0,n):
		adj[i][a] = INF
		adj[a][j] = INF
	adj[j][0] = INF
	adj[j][i] = INF
	return adj	
	
def genNode(root):
	lb = root[0]
	
	bname = root[1]
	i = bname[len(bname)-1]
	adj = root[2]
	ret = []
	for j in range(0,len(adj)):
		if(adj[i-1][j] != INF):
			c = (adj[i-1][j])
			temp = select(adj,i-1,j)
			s  = reduce_all(temp)
			ret.append((lb+s+c,bname + [j+1],temp))
	return ret
	
def startRCM(root):
	n = len(root)
	q = Queue.PriorityQueue()
	count = 1
	adj = copy.deepcopy(root)
	lb = reduce_all(adj)
	bname = []
	bname.append(1) 
	q.put( (lb,bname,adj))
	f = True
	ret = 0
	cost = 0
	while((not q.empty()) and f):
		temp  = q.get()
		genNode(temp)
		x = genNode(temp)
		if(not x):
			f=False
			ret = temp[1]
			cost=temp[0]
		else:
			for y in x:
				q.put(y)
				count+=1
	return (cost,ret,count)
