
def compute_neighbors_cell(board, row, col):
  if board[row][col] == ".":
    return -1

  dirs = [-1, 0, 1]
  neighbors = 0
  for dr in dirs:
    for dc in dirs:
      if dr == 0 and dc == 0:
        continue
      cr = row + dr
      cc = col + dc

      # if board[cr][cc] == "#":
      #   neighbords += 1
      while cr >= 0 and cc >= 0 and cr < len(board) and cc < len(board[0]):
        if board[cr][cc] == "#":
          neighbors += 1
          break
        elif board[cr][cc] == "L":
          break
        cr = cr + dr
        cc = cc + dc

  return neighbors


def compute_neighbors(board):
  neighbors = []
  for row in range(len(board)):
    neighbors.append([])
    for col in range(len(board[row])):
      neighbors[-1].append(compute_neighbors_cell(board, row, col))
  return neighbors


def compute_next_board(board, neighbors):
  next = []
  for row in range(len(board)):
    next.append([])
    for col in range(len(board[row])):
      next_val = "."
      if neighbors[row][col] == 0:
        next_val = "#"
      elif neighbors[row][col] >= 5:
        next_val = "L"
      else:
        next_val = board[row][col]

      next[-1].append(next_val)

  return next


def compare(board, next):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] != next[row][col]:
        return False

  return True


def count_filled(board):
  count = 0
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == "#":
        count += 1
  return count


input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [list(line.strip()) for line in lines]


board = lines
while True:
  neighbor_board = compute_neighbors(board)
  next_board = compute_next_board(board, neighbor_board)
  if compare(board, next_board):
    print(count_filled(board))
    break
  board = next_board
