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
	act(node)
	for neighbor,boolean in enumerate(matrix[node]):
		if boolean:
			dfs(matrix, act, node=neighbor)


def bfs(matrix, act):
	pass
	

# test
res = []
dfs(matrix, res.append)
print(res)