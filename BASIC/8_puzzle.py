class Node:
    def __init__(self, mat, x, y, level, parent):
        self.parent = parent
        self.mat = mat
        self.x = x
        self.y = y
        self.cost = float('inf')
        self.level = level

def print_matrix(mat):
    for row in mat:
        print(' '.join(map(str, row)))

row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

def calculate_cost(initial, final):
    count = 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] != 0 and initial[i][j] != final[i][j]:
                count += 1
    return count

def is_safe(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def print_path(root):
    if root is None:
        return
    print_path(root.parent)
    print_matrix(root.mat)
    print()

def solve(initial, x, y, final):
    pq = []
    root = Node(initial, x, y, 0, None)
    root.cost = calculate_cost(initial, final)
    pq.append(root)

    while pq:
        min_node = min(pq, key=lambda n: n.cost + n.level)
        pq.remove(min_node)

        if min_node.cost == 0:
            print_path(min_node)
            return

        
        for i in range(4):
            new_x, new_y = min_node.x + row[i], min_node.y + col[i]
            if is_safe(new_x, new_y):
                new_mat = [row[:] for row in min_node.mat]
                new_mat[min_node.x][min_node.y], new_mat[new_x][new_y] = new_mat[new_x][new_y], new_mat[min_node.x][min_node.y]
                child = Node(new_mat, new_x, new_y, min_node.level + 1, min_node)
                child.cost = calculate_cost(child.mat, final)
                pq.append(child)


if __name__ == '__main__':
    initial = [
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    final = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    x, y = 0, 1
    solve(initial, x, y, final)
