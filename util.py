from __future__ import print_function
INF = float("inf")

#Mencetak Matrix ke layar
def PrintMatrix(l):
	for i in l:
		for j in i:
			print (j, end = '\t')
		print()

def readFile(fname, adj):
	try:
		infile = open("asset/"+fname+".txt","r")
		strin = infile.read()
		strin = strin.split('\n')
		for stln in strin:
			stln = stln.split()
			l = []
			for c in stln:
				if(int(c) == -999):
					l.append(INF)
				else: 
					l.append(int(c))
			adj.append(l)
	except:
		print("File Not Found")
		exit()
