board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True
            
            b[row][col] = 0
    
    return False


def valid(b, num, pos):
    x = pos[0]
    y = pos[1]

    for i in range(9):
        if b[x][i] == num:
            return False
        
    for i in range(9):
        if b[i][y] == num:
            return False
    
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if b[i+x0][j+y0] == num:
                return False
    
    return True


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)

    return None


def print_board(b):
    for i in range(9):
        if i % 3 == 0:
            print('- - - - - - - - - - - - -')
        line = b[i]
        line = [str(x) for x in line]
        line.insert(0, '|')
        line.insert(4, '|')
        line.insert(8, '|')
        line.insert(12, '|')
        print(' '.join(line))

    print('- - - - - - - - - - - - -')

solve(board)
print_board(board)

