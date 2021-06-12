# Given an integer start and a list edges of pairs of integers.Write a function that computes the lengths of the shortest paths between start and all of the other vertices in the graph using Dijkstra's algorithm and returns them in an array. Each index i in the output array should represent the length of the shortest path between start and vertex i. If no path is found from start to vertex i, then output[i] should be -1.

from heapq import heappush, heappop
from collections import defaultdict as dd
def dijkstrasAlgorithm(start, edges):
	N = len(edges)
	adjacency_list = dd(list)
	
	for u, edge in enumerate(edges):
		for v, w in edge:
			adjacency_list[u].append((v, w))
	
	pq = [(0, start)]
	dist = {}
	
	while pq:
		d, node = heappop(pq)
		if node in dist: continue
		dist[node] = d
		for nei, d2 in adjacency_list[node]:
			if nei not in dist:
				heappush(pq, (d+d2, nei))
	
	return [dist[i] if i in dist else -1 for i in range(N)]
	
	
