from __future__ import print_function
try:
	from PIL import Image
except:
	print("PIL not found, Please install with 'pip install pillowcase'")
	quit()
import rcm
import copy
import util
import btl
import time
import draw



INF = float("inf")

def printPath(l):
	print(l[0],end="")
	for i in range (1,len(l)):
		print("->",l[i],end="",sep="")
	print("->1")
	print()
#Fungsi Main
def Main():
	#Input
	print("1. Reduced Cost Matrix")
	print("2. Bobot Tur Lengkap")
	choice = input(">")
	if(choice == 1):
		pref = "rcm"
		di = True
	elif(choice == 2):
		pref = "blt"
		di = False
	else:
		exit()
	tc = raw_input("Testcase: ")
	fname = pref +"_" +tc
	start = time.time()
	adj = []
	#Load File
	util.readFile(fname,adj)
	print("Input Graph:")
	util.PrintMatrix(adj)
	#Proses
	if(choice == 1):
		ret = rcm.startRCM(adj)
		cost = ret[0]
		count = ret[2]
	else:
		ret = btl.startBNB(adj)
		cost =  ret[0]
		count = ret[2]
	#Output
	print("Cost: ", cost)
	print("Path: ",end ="")
	printPath(ret[1])
	print("Simpul Hidup",count);
	img = draw.draw_graph(adj,ret[1],di,fname)
	ima = Image.open(img)
	ima.show()
	stop = time.time()
	print("Execution Time: ",stop-start,"s",sep="")

	
	
	
#Program Utama untuk memanggil fungsi main
Main()
