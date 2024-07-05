# test out code here and implement in ll.py
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, id, x, y, distance):
        self.id = id
        self.x = x
        self.y = y
        self.distance = distance
        self.children = []

def add_node(graph, parent_id, distance, angle_offset=0):
    parent_node = graph[parent_id]
    
    # Calculate the angle from the center to the parent node
    if parent_node.id == 0:  # Edge case for central node
        angle = np.random.uniform(0, 2 * np.pi)
    else:
        # for rest of the nodes
        center_node = graph[0]
        dx = parent_node.x - center_node.x
        dy = parent_node.y - center_node.y
        angle = np.arctan2(dy, dx)
    
    # Add an offset angle for the new node explained in ll.py
    angle += angle_offset
    
    # Place the new node at the specified distance from the parent node along the calculated angle
    new_x = parent_node.x + distance * np.cos(angle)
    new_y = parent_node.y + distance * np.sin(angle)
    
    new_node_id = len(graph)
    new_node = Node(new_node_id, new_x, new_y, distance)
    graph[new_node_id] = new_node
    parent_node.children.append(new_node)
    return new_node_id

def draw_graph(graph):
    fig, ax = plt.subplots()
    
    drawn_edges = set()  # Set to store pairs of drawn edges
    
    # Draw edges between every pair of nodes
    for node1 in graph.values():
        for node2 in graph.values():
            if node1 != node2:
                edge_pair = frozenset({node1.id, node2.id})  # Use frozenset to make edge order-independent
                if edge_pair not in drawn_edges:
                    ax.plot([node1.x, node2.x], [node1.y, node2.y], 'k-', alpha=0.5)  # 'k-' means black color, solid line
                    drawn_edges.add(edge_pair)  # Add edge pair to drawn edges set
    
    for node in graph.values():
        if node.id == 0:
            ax.plot(node.x, node.y, 'ro')  # Central node
            ax.text(node.x, node.y, 'Center', fontsize=9, ha='right')
        else:
            ax.plot(node.x, node.y, 'bo')  # Other nodes
            ax.text(node.x, node.y, f'{node.distance:.2f}', fontsize=9, ha='right')
            parent_id = next(key for key, val in graph.items() if node in val.children)
            parent_node = graph[parent_id]
            ax.plot([parent_node.x, node.x], [parent_node.y, node.y], 'k-')  # Draw edge to parent node
    
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Initialize graph with the central node
graph = {0: Node(0, 0, 0, 0)}

num_initial_nodes = 10
initial_distances = [5, 7, 10, 6, 9, 8, 7, 10, 6, 8]

# Add initial nodes from the central node
for distance in initial_distances:
    add_node(graph, 0, distance)

# Add more nodes dynamically with varying angles
add_node(graph, 1, 3, np.pi/4)  # Add a node 3 units away from node 1 with an angle offset of pi/4
add_node(graph, 2, 4, -np.pi/3)  # Add a node 4 units away from node 2 with an angle offset of -pi/3
add_node(graph, 3, 2, np.pi/2)  # Add a node 2 units away from node 3 with an angle offset of pi/2

# Draw the graph
draw_graph(graph)
