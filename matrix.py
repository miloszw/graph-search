## DFS and BFS implementations for adjacency matrix


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
	matrix = [[0] * V for _ in range(V)]
	for line in iter(foo, ''):
		s,t = map(int, line.split(' '))
		matrix[s][t] = 1

def dfs(matrix, act, node=0, visited=[]):
	if node in visited:
		return
	visited.append(node)
	act(node)
	for neighbor,boolean in enumerate(matrix[node]):
		if boolean:
			dfs(matrix, act, node=neighbor)


def bfs(matrix, act):
	queue = [0]
	visited = []
	while queue:
		node = queue.pop()
		if node in visited:
			continue
		visited.append(node)
		act(node)
		for neighbor,boolean in enumerate(matrix[node]):
			if boolean:
				queue.append(neighbor)
	

# test
res = []
bfs(matrix, res.append)
print(res)