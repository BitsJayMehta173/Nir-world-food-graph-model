import matplotlib.pyplot as plt
import numpy as np

dict=dict()
class Node:
    def __init__(self, id, x, y, distance,value):
        self.id = id
        self.x = x
        self.y = y
        self.distance = distance
        self.value = value
        self.children = []

def add_node(graph, parent_id, distance,i):

    # for now we are adding all the new nodes with parent_id 0 but we need to optimize to save space by connecting it with nearest node with distance closer to center or its parent

    parent_node = graph[parent_id]
    
    # Calculate the angle from the center to the center node for now i have used random 0 to 360
    angle = np.random.uniform(0, 2 * np.pi)
    while angle in dict[0]:    
        angle = np.random.uniform(0, 2 * np.pi)
    # dict[i].append(angle)
    dict[0].append(angle)


    # Place the new node at the specified distance from the center node along the calculated angle
    new_x = parent_node.x + distance * np.cos(angle)
    new_y = parent_node.y + distance * np.sin(angle)
    value=10
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
# num_initial_nodes = 10
# initial_distances = [5, 7, 10, 6, 9, 8, 7, 10, 6, 8]

# Add initial nodes from the central node
# for now i am using loop to create new as nodes as much as i like with the same distance multiplied by range of random number between (index-1 to index) of loop which creates 
maxdist=1
dict[0]=[]
for i in range(1,3):
    # dict[i-1]=[]
    dist=maxdist
    for j in range(10):
        distance=np.random.uniform(dist+30,dist+100)
        add_node(graph, 0,distance,i-1)
        if distance>maxdist:
            maxdist=distance
        

# Draw the graph
draw_graph(graph)