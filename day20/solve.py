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

# print(len(to_use))
# print(explored)


edge_counts = {}
for used_piece in explored:
  edges = tiles[used_piece[0]][used_piece[1]]
  for edge in edges:
    if edge not in edge_counts:
      edge_counts[edge] = 0
    edge_counts[edge] += 1

corners = 0
product = 1
for used_piece in explored:
  edges = tiles[used_piece[0]][used_piece[1]]
  num_ones = 0
  for edge in edges:
    if edge_counts[edge] == 1:
      num_ones += 1

  # if num_ones == 0:
  #   print("internal", used_piece)
  # elif num_ones == 1:
  #   print("edge", used_piece)
  if num_ones == 2:
    print("corner", used_piece)
    corners += 1
    product *= int(used_piece[0])
  # else:
  #   print("something fucked", used_piece, num_ones)

# print(corners)

print(product)
