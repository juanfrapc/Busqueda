# Search methods

import search

def busca(a,b):
	ab = search.GPSProblem(a, b, search.romania)

	sol = search.breadth_first_graph_search(ab)
	print "\nAnchura: nodos exapndidos = " + str(sol[1])
	print sol[0].path()

	sol = search.depth_first_graph_search(ab)
	print "\nProfundidad: nodos exapndidos = " + str(sol[1])
	print sol[0].path()

	sol = search.branch_and_bound(ab)
	print "\nRamificacion y acotacion: nodos exapndidos = " + str(sol[1])
	print sol[0].path()

	sol = search.branch_and_bound_sub(ab)
	print "\nRamificacion y acotacion con subestimacion: nodos exapndidos = " + str(sol[1])
	print sol[0].path()

	print '==================================================================================='

'''
print "\nBusqueda iterativa"
print search.iterative_deepening_search(ab).path()
print "\nProfundidad limitada"
print search.depth_limited_search(ab).path()
'''

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

lista=search.romania.locations.keys()
lista.sort()
for ori in lista:
	print "------------------------------------------------------------------------------"
	for des in lista:
		if ori != des:
			print "Desde %s hasta %s" % (ori, des)
			busca(ori,des)

busca('O','E')




