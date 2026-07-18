import sys

from graph_dfs_112 import Graph, DFSPaths

def main():

    V = int(sys.stdin.readline().strip())

    g = Graph(V)

    for line in sys.stdin:
        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

    dfs = DFSPaths(g, 4)

    print(dfs.hasPathTo(2))

    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()
