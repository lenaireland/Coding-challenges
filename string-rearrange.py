"""Given an array of equal-length strings, check if it is possible to rearrange 
the strings in such a way that after the rearrangement the strings at 
consecutive positions would differ by exactly one character."""

class Node:
    """String node"""
    
    def __init__(self, name, adjacent=None):
        
        if adjacent is None:
            adjacent = set()
            
        self.name = name
        self.adjacent = adjacent
    
    def __repr__(self):
        return "<Node: {}>".format(self.name)

class Graph:
    """Graph holding relationships"""
    
    def __init__(self):
        self.nodes = set()

    def __repr__(self):
        return "<Graph: {}>".format([n.name for n in self.nodes])
        
    def add_node(self, node):
        self.nodes.add(node)
        
    def add_adj(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)
        
def is_path(graph, current, path=None):
    
    if path is None:
        path = [current]
    else:
        path.append(current)
        
    if set(path) == graph.nodes:
        # print("got here path:{}".format(path))
        # print("got here graph:{}".format(graph.nodes))
        return True
    
    for node in current.adjacent - set(path):
        # print("current:{}".format(current))
        # print("node:{}".format(node))
        # print("path:{}".format(path))
        
        if is_path(graph, node, path):
            return True
        else:
            path.remove(node)
            # print(path)
    
    return False
    

def stringsRearrangement(inputArray):
    
    # create graph
    graph = Graph()
    
    # create nodes
    for string in inputArray:
        node = Node(string)
        graph.nodes.add(node)
        
    print(graph.nodes)
    
    # create adjacency sets
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            
            if node1 == node2:
                continue
            else:
                diff = 0
                for k in range(len(node1.name)):
                    if node1.name[k] != node2.name[k]:
                        diff += 1
                if diff == 1:
                    graph.add_adj(node1, node2)
                    
        # print(node1.adjacent)

    # traverse graph to determine if rearrangement possible         
    for node in graph.nodes:
        # print("firstnode:{}".format(node))
        if is_path(graph, node):
            return True
    
    return False
