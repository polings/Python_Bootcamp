import argparse
from collections import deque

from src.utils import load_graph


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Enable logging of the found path')
    parser.add_argument('--from', type=str, default="Erdős number",
                        help='The name of an existing article from where you want to start searching', dest='start')
    parser.add_argument('--to', type=str, default="Mental_disorder",
                        help='The name of an existing article to what you want to search', dest='end')
    parser.add_argument('--non-directed', action='store_true', default=False,
                        help='Specify if the graph is non-directed')
    return parser.parse_args()


def find_path(graph, start: str, end: str) -> list:
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [start])])
    f = graph.successors if graph.is_directed() else graph.neighbors
    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        neighbors = f(node)
        for neighbor in neighbors:
            if neighbor == end:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))

    return []


def pretty_print(path: list):
    if path:
        print(repr(path[0].replace('_', ' ')), end='')
        for i in range(1, len(path)):
            print(f" -> {repr(path[i].replace('_', ' '))}", end='')
        print()


def main():
    args = parse_arguments()
    graph = load_graph(args.non_directed)

    path_between_nodes = find_path(graph, args.start, args.end)
    if not path_between_nodes:
        print("Path not found.")
    else:
        if args.verbose:
            pretty_print(path_between_nodes)
        print(len(path_between_nodes) - 1)


if __name__ == '__main__':
    main()
