## DFS and BFS implementations for adjacency list


# ignore lines with leading #
def ignore_comments(func):
	def inner(*args):
		while True:
			res = func(*args)
			if not res or res[0] != "#":
				return res
	return inner

# read graph
from sys import argv
with open(argv[1]) as f:
	foo = ignore_comments(f.readline)
	V,E = map(int, foo().split(' '))
	adj_list = [[] for _ in range(V)]
	for line in iter(foo, ''):
		s,t = map(int, line.split(' '))
		adj_list[s].append(t)
		

def dfs(adj_list, act, node=0, visited=[]):
	if node in visited:
		return
	visited.append(node)
	act(node)
	for neighbor in adj_list[node]:
		dfs(adj_list, act, node=neighbor)


def bfs(adj_list, act):
	queue = [0]
	visited = []
	while queue:
		node = queue.pop()
		if node in visited:
			continue
		visited.append(node)
		act(node)
		for neighbor in adj_list[node]:
			queue.append(neighbor)
	

# test
# res = []
# bfs(adj_list, res.append)
# print(res)