import numpy
from random import choice
class Node:
    def _init_(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.a = 0
        self.b = 0
        self.c = 0
    def _moving_(self, other):
        return self.position == other.position
def return_path(current_node, maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    result = [[-1 for i in range(no_columns)], j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current_parent
    path = path[::-1]
    start_value = 0
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result
def search(maze, cost, start, end):
    start_node = Node(None, tuple(start))
    start_node.a = start_node.b = start_node.c = 0
    end_node = Node(None, tuple(end))
    end_node.a = end_node.b = end_node.c = 0
    
    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_list.append(start_node)
    
    outer_interations = 0
    max_interations = (len(maze) // 2)**10
    move = [[-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]]
    no_rows, no_columns = np.shape(maze)
    
    while len(yet_to_visit_list) > 0:
        outer_interations += 1
        
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.c < current_node.c:
                current_node = item
                current_index = index
        
        if outer_interations > max_interations:
            print("I DON'T THINK SO...")
            return return_path(current_node, maze)
        
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)
        
        if current_node == end_node:
            return return_path(current_node, maze)
        
        babycs = []

        for new_position in move:
            node_position = (current_node.position[0] +new_position[0], current_node.position[1]+new_position[1])
    
            if (node_position[0] > (no_rows-1) or node_position[0]<0 or node_position[1] > (no_columns - 1) or node_position[1]< 0):
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
    
            babycs.append(new_node)
    
    for baby in babycs:
        if len([visited_baby for visited_baby in visited_list if visited_baby == baby]) > 0:
            continue
        baby.a = current_node.a + cost
        
        baby.b = (((baby.position[0] - end_node.position[0])**2) + ((baby.position[1] - end_node.position[1])**2))
        babu.c = baby.a + baby.b
        
        if len([i for i in yet_to_visit_list if baby == i and child.a > i.a]) > 0:
            continue
        yet_to_visit_list.append(baby)
if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0 ,0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0]]
    start = [0, 0]
    end = [7, 7]
    cost = 1
    
    path = search(maze, cost, start, end)
    print(path)
