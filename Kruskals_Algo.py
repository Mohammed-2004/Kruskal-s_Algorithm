class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        # Sort edges by weight
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        result = []

        # Initialize disjoint sets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Iterate through sorted edges
        for edge in self.edges:
            u, v, w = edge
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append(edge)
                self.union(parent, rank, x, y)

        # Print MST result
        print("\nEdges in MST:")
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")


# Main function to ensure the exact input-output format you want
if __name__ == "__main__":
    # Input the number of vertices
    vertices = int(input("Enter the number of vertices: "))
    edges_count = int(input("Enter the number of edges: "))

    graph = Graph(vertices)

    print("Enter the edges (source destination weight), one per line:")
    for _ in range(edges_count):
        edge = input().strip()  # Take the edge input
        u, v, w = map(int, edge.split())  # Split the input into source, destination, and weight
        graph.add_edge(u, v, w)  # Add the edge to the graph

    graph.kruskal_mst()
