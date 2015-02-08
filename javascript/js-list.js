// Simple javascript implementation of dfs and bfs for adj lists.

var input = "\
# start vertice, end vertice\
\n0 1\
\n1 2\
\n0 3\
\n1 3\
\n3 1\
";

var list = [];

var lines = input.split('\n');
for (var i in lines) {
	line = lines[i];
	if (line[0] == "#")
		continue;
	nodes = line.split(' ');
	if (!list[+nodes[0]])
		list[+nodes[0]] = [];
	list[+nodes[0]].push(+nodes[1]);
}

// for (var i in list) {
// 	print("[" + list[i] + "]");
// }

var dfs = function(list, act, node, visited) {
	node = node || 0;
	visited = visited || [];
	if (visited.indexOf(node) !== -1)
		return;
	visited.push(node);
	act(node);
	for (var i in list[node]) {
		dfs(list, act, list[node][i], visited);
	}
}

var bfs = function(list, act, node) {
	node = node || 0;
	queue = [node];
	visited = [];
	while (queue.length > 0) {
		node = queue.pop();
		if (visited.indexOf(node) !== -1)
			continue;
		visited.push(node);
		act(node);
		for (var i in list[node]) {
			queue.push(list[node][i]);
		}
	}
}

// Test
// bfs(list, function(el) {
// 	print(el);
// });