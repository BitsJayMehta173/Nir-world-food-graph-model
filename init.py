class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []
        self.visited = False
        self.distance = dict()
        self.previous = None
        self.angle=[]

    def add_neighbor(self, neighbor):

        # only two nodes are required to plot the angle 

        if len(self.angle)==2:
            self.angle.append(60)
        else:
            self.angle.append(neighbor.value)
        self.adjacent.append(neighbor)
        if neighbor in self.distance:
            self.distance[neighbor].append(10)
        else:
            self.distance[neighbor]=[]
            self.distance[neighbor].append(10)

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return str(self)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            new_node = Node(value)
            self.nodes[value] = new_node
        return self.nodes[value]

    def add_edge(self, value1, value2):
        node1 = self.add_node(value1)
        node2 = self.add_node(value2)
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def remove_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            node1 = self.nodes[value1]
            node2 = self.nodes[value2]
            if node2 in node1.adjacent:
                node1.adjacent.remove(node2)
            if node1 in node2.adjacent:
                node2.adjacent.remove(node1)

    def remove_node(self, value):
        if value in self.nodes:
            node_to_remove = self.nodes[value]
            for node in self.nodes.values():
                if node_to_remove in node.adjacent:
                    node.adjacent.remove(node_to_remove)
            del self.nodes[value]

    def get_nodes(self):
        return list(self.nodes.keys())

    def get_edges(self):
        edges = []
        for node in self.nodes.values():
            for neighbor in node.adjacent:
                if {node.value, neighbor.value} not in edges:
                    edges.append({node.value, neighbor.value})
        return edges


    # cooresponds to print(g)
    def __str__(self):
        result = ""
        for node in self.nodes.values():
            result += f"{node.value} -> {[neighbor.value for neighbor in node.adjacent]}\n"
        return result

g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
print(g)
