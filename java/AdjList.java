import java.io.*;
import java.util.*;

class AdjList {
	public static void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Usage: java List <graph file>");
			System.exit(1);
		}
		// read graph file
		HashMap<Integer,LinkedList<Integer>> list = new HashMap<>();
		try {
			BufferedReader reader = new BufferedReader(new FileReader(args[0]));
			String[] s = readLine(reader).split(" ");
			int V = Integer.valueOf(s[0]);
			int E = Integer.valueOf(s[1]);
			String line;
			int from, to;
			while ((line = readLine(reader)) != null) {
				s = line.split(" ");
				from = Integer.valueOf(s[0]);
				to = Integer.valueOf(s[1]);
				if (list.get(from) == null)
					list.put(from, new LinkedList<Integer>());
				list.get(from).add(to);
			}
		} catch (IOException e) {
			System.out.println("File not found.");
			System.exit(1);
		}

		// test
		Actor<Integer> foo = new Actor<Integer>() {
			public void call(Integer i) {
				System.out.println(i);
				return;
			}
		};
		bfs(list, foo, 0);

	}

	private static String readLine(BufferedReader r) throws IOException {
		// ignore lines with leading '#'
		String res;
		while ((res = r.readLine()) != null && res.substring(0,1).equals("#"));
		return res;
	}

	public interface Actor<T> {
		public void call(T arg);
	}

	public static <T> void dfs(Map<Integer,LinkedList<Integer>> list, Actor<Integer> act, 
		LinkedList<Integer> visited, Integer node) {
		if (visited.contains(node))
			return;
		visited.add(node);
		act.call(node);
		LinkedList<Integer> neighbors = list.get(node);
		if (neighbors == null)
			return;
		for (int neighbor : neighbors)
			dfs(list, act, visited, neighbor);
	}

	public static <T> void bfs(Map<Integer,LinkedList<Integer>> list, Actor<Integer> act,
		Integer node) {
		LinkedList<Integer> visited = new LinkedList<Integer>();
		LinkedList<Integer> queue = new LinkedList<Integer>(Arrays.asList(node));
		LinkedList<Integer> neighbors;
		try {
			while (true) {
				node = queue.pop();
				if (visited.contains(node))
					continue;
				visited.add(node);
				act.call(node);
				neighbors = list.get(node);
				if (neighbors == null)
					continue;
				for (int neighbor : neighbors)
					queue.add(neighbor);
			}
		} catch (Exception e) {
			// queue is empty, quit
		}
	}
}