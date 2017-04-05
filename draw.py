try:
	from graph_tool.all import *
except:
	print("Please Install graph-tool for Python from https://graph-tool.skewed.de")
import networkx as nx
import matplotlib.pyplot as plt

INF = float("inf")

def draw_graph(adj,path,di,fname):
	g = Graph(directed=di)
	vprop = g.new_vertex_property("string") 
	eprop = g.new_edge_property("string")
	vprop_color = g.new_vertex_property("string")
	eprop_color = g.new_edge_property("string")
	n = len(adj)
	l = []
	#Add Vertex
	for i in range(0,n):
		temp = g.add_vertex()
		vprop[temp] = i+1
		vprop_color[temp] = "black"
	#Dummy Vertex untuk Mendapatkan Circular Layout
	root = g.add_vertex()
	vprop[root] = "x"
	vprop_color[root]="none"
	
	#Add Edge
	for i in range(0,n):
		if(not di):
			for j in range(i,n):
				if(adj[i][j] != INF):
					temp = g.add_edge(g.vertex(i),g.vertex(j))
					eprop[temp] = adj[i][j]
					eprop_color[temp]= "black"
		else:
			for j in range(0,n):
				if(adj[i][j] != INF):
					temp = g.add_edge(g.vertex(i),g.vertex(j))
					eprop[temp] = adj[i][j]
					eprop_color[temp]= "black"
	#Dummy Edge ke dummy Vertex agar terbentuk bentuk circular
	for i in range(0,n):
		temp = g.add_edge(root,g.vertex(i))
		eprop_color[temp] = "none"
	#Mengubah warna path menjadi merah
	for i in range(0,len(path)):
		src = g.vertex(path[i]-1)
		i = (i+1)%len(path)
		dest = g.vertex(path[i]-1) 
		eprop_color[g.edge(src,dest)] = "red"
	try:
		os.mkdir("out")
	except:
		dummy=0
	#Render Graf
	g.vertex_properties["name"]=vprop 
	g.edge_properties["weight"]=eprop 
	g.vertex_properties["color"]=vprop_color
	g.edge_properties["color"]=eprop_color
	x=  g.vertex_properties["color"]
	oname="out/"+fname+".png"
	graph_draw(
    g,
    pos=radial_tree_layout(g,n),
    vertex_text=g.vertex_properties["name"],
    vertex_font_size=40,
    vertex_color="none",
	vertex_fill_color=x,
	edge_pen_width=5.0,
	edge_text=g.edge_properties["weight"],
	edge_font_size=12,
	edge_color=g.edge_properties["color"],
    output_size=(1000,1000), 
	output = oname,
	bg_color=[1,1,1,1]
	)
	return oname
					
