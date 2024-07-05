import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, id, x, y, distance,value):
        self.id = id
        self.x = x
        self.y = y
        self.distance = distance
        self.value = value
        self.children = []

def add_node(graph, parent_id, distance, angle_offset=0):
    parent_node = graph[parent_id]
    
    # Calculate the angle from the center to the parent node
    if parent_node.id == 0:  # Special case for central node
        angle = np.random.uniform(0, 2 * np.pi)
    else:
        center_node = graph[0]
        dx = parent_node.x - center_node.x
        dy = parent_node.y - center_node.y
        angle = np.arctan2(dy, dx)
    
    # Add an offset angle for the new node and add angle_offset which is opposite of center and parent node which will be (0 to 180) (0,np.pi/2)
    angle += angle_offset
    
    # Place the new node at the specified distance from the parent node along the calculated angle
    new_x = parent_node.x + distance * np.cos(angle)
    new_y = parent_node.y + distance * np.sin(angle)
    value=40
    new_node_id = len(graph)
    new_node = Node(new_node_id, new_x, new_y, distance,value)
    graph[new_node_id] = new_node
    parent_node.children.append(new_node)
    return new_node_id

def draw_graph(graph):
    fig, ax = plt.subplots()
    
    for node in graph.values():
        if node.id == 0:
            ax.plot(node.x, node.y, 'ro')  # Central node
            ax.text(node.x, node.y, 'Center', fontsize=9, ha='right')
        else:
            ax.plot(node.x, node.y, 'bo')  # Other nodes
            ax.text(node.x, node.y, f'{node.distance:.2f}', fontsize=9, ha='right')
            parent_id = next(key for key, val in graph.items() if node in val.children)
            parent_node = graph[parent_id]
            # since we are storing x,y for all from centre itself we can also decrease it by just keeping record of parent_node and distance from it but here we are drawing line from parent_node x,y to node x,y
            ax.plot([parent_node.x, node.x], [parent_node.y, node.y], 'k-')
    
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Initialize graph with the central node
# for now i have initialized food quantity as 10
graph = {0: Node(0, 0, 0, 0,10)}

# taken 10 nodes in the area of circle
num_initial_nodes = 10
initial_distances = [5, 7, 10, 6, 9, 8, 7, 10, 6, 8]

# Add initial nodes from the central node
for distance in initial_distances:
    add_node(graph, 0, distance)

# Add more nodes dynamically and as we have added angle between 0 to 1
add_node(graph, 1, 3, np.random.uniform(0,np.pi/2))  # Add a node 3 units away from node 1 with an angle offset of pi/4
add_node(graph, 2, 4, np.random.uniform(0,np.pi/2))  # Add a node 4 units away from node 2 with an angle offset of -pi/3
add_node(graph, 3, 2, np.random.uniform(0,np.pi/2))  # Add a node 2 units away from node 3 with an angle offset of pi/2

# Draw the graph
draw_graph(graph)
