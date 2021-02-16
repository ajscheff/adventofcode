input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [list(line.strip()) for line in lines]

board = [[lines]]

def pad_sl(amt, sl):
  row_padding = ['.'] * amt
  for i in range(len(sl)):
    new_row = row_padding[:]
    new_row.extend(sl[i])
    new_row.extend(row_padding)
    sl[i] = new_row

  new_row = ['.'] * len(sl[0])
  new_rows = [new_row] * amt
  return new_rows + sl + new_rows

def pad_cube(amt, cube):
  for i in range(len(cube)):
    cube[i] = pad_sl(amt, cube[i])

  new_row = ['.'] * len(cube[0][0])
  new_sl = [new_row] * len(cube[0])
  new_sls = [new_sl] * amt
  return new_sls + cube + new_sls
  
def pad_board(amt, board):
  for i in range(len(board)):
    board[i] = pad_cube(amt, board[i])
  
  new_row = ['.'] * len(board[0][0][0])
  new_sl = [new_row] * len(board[0][0])
  new_cu = [new_sl] * len(board[0])
  new_cus = [new_cu] * amt
  return new_cus + board + new_cus

def compute_neighbors_cell(board, cu, sl, row, col):
  dirs = [-1, 0, 1]
  neighbors = 0
  for dcu in dirs:
    for ds in dirs:
      for dr in dirs:
        for dc in dirs:
          if dcu == 0 and ds == 0 and dr == 0 and dc == 0:
            continue
          ccu = cu + dcu
          cs = sl + ds
          cr = row + dr
          cc = col + dc

          if ccu >= 0 and cs >= 0 and cr >= 0 and cc >= 0 and ccu < len(board) and cs < len(board[0]) and cr < len(board[0][0]) and cc < len(board[0][0][0]):
            if board[ccu][cs][cr][cc] == "#":
              neighbors += 1
          
  return neighbors

def compute_neighbors(board):
  neighbors = []
  for cu in range(len(board)):
    neighbors.append([])
    for sl in range(len(board[cu])):
      neighbors[-1].append([])
      for row in range(len(board[cu][sl])):
        neighbors[-1][-1].append([])
        for col in range(len(board[cu][sl][row])):
          neighbors[-1][-1][-1].append(compute_neighbors_cell(board, cu, sl, row, col))

  return neighbors
  
def compute_next_board(board, neighbors):
  next = []
  for cu in range(len(board)):
    next.append([])
    for sl in range(len(board[cu])):
      next[-1].append([])
      for row in range(len(board[cu][sl])):
        next[-1][-1].append([])
        for col in range(len(board[cu][sl][row])):
          next_val = "."
          bv = board[cu][sl][row][col]
          nv = neighbors[cu][sl][row][col]
          if nv == 3:
            next_val = "#"
          elif nv == 2:
            next_val = bv
          else:
            next_val = "."

          next[-1][-1][-1].append(next_val)

  return next

def print_sl(sl):
  for row in sl:
    print("".join(row))

def print_cube(cube):
  for sl in cube:
    print_sl(sl)
    print("")

def print_board(board):
  for cube in board:
    print("CUBE START")
    print_cube(cube)
    print("CUBE END")


board = pad_board(6, board)

# print_board(board)

for i in range(6):
  neighbors = compute_neighbors(board)
  next_board = compute_next_board(board, neighbors)
  board = next_board

count = 0
for cu in board:
  for sl in cu:
    for row in sl:
      for col in row:
        if col == "#":
          count += 1


print(count)