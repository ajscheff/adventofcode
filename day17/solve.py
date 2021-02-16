input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [list(line.strip()) for line in lines]

board = [lines]

def pad_sl(amt, sl):
  row_padding = ['.'] * amt
  print_sl(sl)
  for i in range(len(sl)):
    new_row = row_padding[:]
    new_row.extend(sl[i])
    new_row.extend(row_padding)
    sl[i] = new_row
  print_sl(sl)

  new_row = ['.'] * len(sl[0])
  new_rows = [new_row] * amt
  new_sl = new_rows + sl + new_rows
  return new_sl

def pad_board(amt, board):
  for i in range(len(board)):
    board[i] = pad_sl(amt, board[i])

  new_row = ['.'] * len(board[0][0])
  new_sl = [new_row] * len(board[0])
  new_sls = [new_sl] * amt
  return new_sls + board + new_sls
  

def compute_neighbors_cell(board, sl, row, col):
  dirs = [-1, 0, 1]
  neighbors = 0
  for ds in dirs:
    for dr in dirs:
      for dc in dirs:
        if ds == 0 and dr == 0 and dc == 0:
          continue
        cs = sl + ds
        cr = row + dr
        cc = col + dc

        if cs >= 0 and cr >= 0 and cc >= 0 and cs < len(board) and cr < len(board[0]) and cc < len(board[0][0]):
          if board[cs][cr][cc] == "#":
            neighbors += 1
          
  return neighbors

def compute_neighbors(board):
  neighbors = []
  for sl in range(len(board)):
    neighbors.append([])
    for row in range(len(board[sl])):
      neighbors[-1].append([])
      for col in range(len(board[sl][row])):
        neighbors[-1][-1].append(compute_neighbors_cell(board, sl, row, col))

  return neighbors
  
def compute_next_board(board, neighbors):
  next = []
  for sl in range(len(board)):
    next.append([])
    for row in range(len(board[sl])):
      next[-1].append([])
      for col in range(len(board[sl][row])):
        next_val = "."
        bv = board[sl][row][col]
        nv = neighbors[sl][row][col]
        if nv == 3:
          next_val = "#"
        elif nv == 2:
          next_val = bv
        else:
          next_val = "."

        next[-1][-1].append(next_val)

  return next
def print_sl(sl):
  for row in sl:
    print("".join(row))

def print_board(board):
  for sl in board:
    print_sl(sl)
    print("")


board = pad_board(6, board)

print_board(board)

for i in range(6):
  neighbors = compute_neighbors(board)
  next_board = compute_next_board(board, neighbors)
  board = next_board

count = 0
for sl in board:
  for row in sl:
    for col in row:
      if col == "#":
        count += 1


print(count)