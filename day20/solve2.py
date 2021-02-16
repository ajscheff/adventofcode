from math import floor

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

tile_lines = {}
current_tile_id = 0
current_tile = []
for line in lines:
  if line[:4] == "Tile":
    current_tile_id = line[5:-1]
  elif line == "":
    tile_lines[current_tile_id] = current_tile
    current_tile = []
  else:
    current_tile.append(line)

tile_lines[current_tile_id] = current_tile


def edges_from_tile(tile):
  top = tile[0]
  right = "".join([line[-1] for line in tile])
  bottom = tile[-1][::-1]
  left = "".join([line[0] for line in tile])[::-1]
  return [[top, right, bottom, left], [top[::-1], left[::-1], bottom[::-1], right[::-1]]]


tiles = {}
for tile_id in tile_lines:
  tiles[tile_id] = edges_from_tile(tile_lines[tile_id])

edge_to_pieces = {}
for tile_id in tiles:
  tile = tiles[tile_id]
  for i in range(len(tile)):
    for edge in tile[i]:
      if edge not in edge_to_pieces:
        edge_to_pieces[edge] = []
      edge_to_pieces[edge].append([tile_id, i])

# print(edge_to_pieces)

to_use = set(tiles.keys())

to_explore = [[to_use.pop(), 1]]
explored = []
while len(to_explore) > 0:
  curr = to_explore.pop()
  explored.append(curr)
  edges = tiles[curr[0]][curr[1]][:]
  for edge in edges:
    pieces = edge_to_pieces[edge]
    for piece in pieces:
      if piece[0] in to_use:
        to_use.remove(piece[0])
        to_explore.append([piece[0], piece[1]])


edge_counts = {}
for used_piece in explored:
  edges = tiles[used_piece[0]][used_piece[1]]
  for edge in edges:
    if edge not in edge_counts:
      edge_counts[edge] = 0
    edge_counts[edge] += 1


def get_right_edge(piece):
  pid = piece[0]
  flip = piece[1]
  rot = piece[2]
  return tiles[pid][flip][(1-rot) % 4]


def get_bottom_edge(piece):
  pid = piece[0]
  flip = piece[1]
  rot = piece[2]
  return tiles[pid][flip][(2-rot) % 4]


def find_rotation_right(prev_right, curr):
  edges = tiles[curr[0]][curr[1]]
  index_match = edges.index(prev_right[::-1])
  return 3 - index_match


def find_rotation_bottom(prev_bottom, curr):
  edges = tiles[curr[0]][curr[1]]
  index_match = edges.index(prev_bottom[::-1])
  return (-index_match) % 4


for edge in tiles["3931"][0]:
  print(edge, edge_counts[edge])

initial = ["3343", 0, 3]
# initial = ["3323", 1, 1]
# initial = ["3931", 0, 1]
# initial = ["3221", 0, 2]

arrayed = [[initial]]


def find_neighbor(previous_id, edge):
  next_pieces = edge_to_pieces[edge[::-1]]

  next_piece = next_pieces[0]
  edge = True
  if len(next_pieces) == 2:
    edge = False
    if next_pieces[0][0] == previous_id:
      next_piece = next_pieces[1]

  return (next_piece, edge)


def add_row():
  while True:
    previous = arrayed[-1][-1]
    right_edge = get_right_edge(previous)
    next_piece, edge = find_neighbor(previous[0], right_edge)
    if edge:
      break

    next_rot = find_rotation_right(right_edge, next_piece)
    arrayed[-1].append([next_piece[0], next_piece[1], next_rot])


while True:
  add_row()

  bottom_edge = get_bottom_edge(arrayed[-1][0])
  next_piece, bottom = find_neighbor(arrayed[-1][0][0], bottom_edge)
  if bottom:
    break

  next_rot = find_rotation_bottom(bottom_edge, next_piece)
  arrayed.append([[next_piece[0], next_piece[1], next_rot]])


def get_from_tile(tile, row_index, col_index):

  if tile[1] == 1:
    col_index = 9 - col_index

    for i in range(tile[2]):
      old_row = row_index
      # col_index = row_index
      row_index = col_index
      col_index = 9 - old_row

  else:
    for i in range(tile[2]):
      old_col = col_index
      col_index = row_index
      row_index = 9 - old_col

  return tile_lines[tile[0]][row_index][col_index]


bitmap = []
raccum = []

for row in range(120):
  tile_row_index = row / 10
  row_index = row % 10

  if row_index == 0 or row_index == 9:
    continue

  for col in range(120):

    tile_col_index = col / 10
    col_index = col % 10

    if col_index == 0 or col_index == 9:
      continue

    tile = arrayed[tile_row_index][tile_col_index]
    raccum.append(get_from_tile(tile, row_index, col_index))

  bitmap.append("".join(raccum))
  raccum = []


def print_board(bitmap):
  for i in range(len(bitmap)):
    if i % 10 == 0:
      print("")
    # if i == 10:
    #   break
    s = []
    for j in range(len(bitmap[i])):
      if j % 10 == 0:
        s.append(" ")
      s.append(bitmap[i][j])

    print("".join(s))


# print_board(bitmap)
# for tile in arrayed[0]:
#   print(tile)
#   for tr in tile_lines[tile[0]]:
#     print(tr)
#   print("===")


sea_monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]


test_bm = [".#.#..#.##...#.##..#####", "###....#.#....#..#......", "##.##.###.#.#..######...", "###.#####...#.#####.#..#", "##.#....#.##.####...#.##", "...########.#....#####.#", "....#..#...##..#.#.###..", ".####...#..#.....#......", "#..#.##..#..###.#.##....", "#.####..#.####.#.#.###..", "###.#.#...#.######.#..##", "#.####....##..########.#",
           "##..##.#...#...#.#.#.#..", "...#..#..#.#.##..###.###", ".#.#....#.##.#...###.##.", "###.#...#..#.##.######..", ".#.#.###.##.##.#..#.##..", ".####.###.#...###.#..#.#", "..#.#..#..#.#.#.####.###", "#..####...#.#.#.###.###.", "#####..#####...###....##", "#.##..#..#...#..####...#", ".#.###..##..##..####.##.", "...###...##...#...#..###"]


def is_sm(sea_monster, bitmap, row, col):
  for sr in range(len(sea_monster)):
    for sc in range(len(sea_monster[0])):
      if sea_monster[sr][sc] == "#":
        if bitmap[row + sr][col + sc] == ".":
          return False
  return True


def count_sm(sea_monster, bitmap):
  count = 0
  sms = []
  for row in range(len(bitmap) - len(sea_monster)):
    for col in range(len(bitmap[0]) - len(sea_monster[0])):
      if is_sm(sea_monster, bitmap, row, col):
        count += 1
        sms.append([row, col])

  return (count, sms)


def convert_bm(bitmap):
  bms = [bitmap]

  for i in range(3):
    previous = bms[-1]
    print(len(previous), len(previous[0]))
    new = []
    for row in range(len(bitmap)):
      r = []
      for col in range(len(bitmap[row])):
        r.append(previous[len(bitmap)-col-1][row])
      new.append("".join(r))

    bms.append(new)

  return bms


bms = convert_bm(bitmap)

for bm in bms:
  count, sms = count_sm(sea_monster, bm)
  if count > 0:
    total = 0
    for row in bm:
      for col in row:
        if col == "#":
          total += 1
    print(total - count * 15)

count = 0
for row in bitmap:
  for col in row:
    if col == "#":
      count += 1

# print(count)


# print_board(bms[3])
# print("======")
# print_board(bms[3][::-1])


# for row in arrayed:
#   just_ids = map(lambda x: x[0], row)
#   print(",".join(just_ids))

# corners = 0
# product = 1
# for used_piece in explored:
#   edges = tiles[used_piece[0]][used_piece[1]]
#   num_ones = 0
#   for edge in edges:
#     if edge_counts[edge] == 1:
#       num_ones += 1

#   # if num_ones == 0:
#   #   print("internal", used_piece)
#   # elif num_ones == 1:
#   #   print("edge", used_piece)
#   if num_ones == 2:
#     print("corner", used_piece)
#     corners += 1
#     product *= int(used_piece[0])
#   # else:
#   #   print("something fucked", used_piece, num_ones)

# # print(corners)

# print(product)
