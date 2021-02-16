input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

instructions = [[line[0], int(line[1:])] for line in lines]

waypoint = [10, 1]
position = [0, 0]


def get_direction(pos, way):
  return [way[0] - pos[0], way[1] - pos[1]]


def compute_waypoint(pos, way, deg):
  direction = get_direction(pos, way)
  if deg == 0:
    print("rotate by 0")
    return way
  elif deg == 90:
    return [pos[0] - direction[1], pos[1] + direction[0]]
  elif deg == 180:
    return [pos[0] - direction[0], pos[1] - direction[1]]
  elif deg == 270:
    return [pos[0] + direction[1], pos[1] - direction[0]]
  else:
    print("weird rotation")


for ins in instructions:
  print(ins)

  com = ins[0]
  arg = ins[1]

  direction = get_direction(position, waypoint)

  if com == "N":
    waypoint[1] += arg
  elif com == "S":
    waypoint[1] -= arg
  elif com == "E":
    waypoint[0] += arg
  elif com == "W":
    waypoint[0] -= arg
  elif com == "L":
    # direction = (direction + arg) % 360
    waypoint = compute_waypoint(position, waypoint, arg)
  elif com == "R":
    # direction = (direction - arg) % 360
    waypoint = compute_waypoint(position, waypoint, 360-arg)

  elif com == "F":
    # if direction == 0:
    #   position[0] += arg
    # elif direction == 90:
    #   position[1] += arg
    # elif direction == 180:
    #   position[0] -= arg
    # elif direction == 270:
    #   position[1] -= arg
    # else:
    #   print("Direction is weird", direction)
    position[0] = position[0] + arg * direction[0]
    position[1] = position[1] + arg * direction[1]
    waypoint[0] = position[0] + direction[0]
    waypoint[1] = position[1] + direction[1]

  else:
    print("Weird command", ins)

  print(position, waypoint)

  print("==============")

  # if ins == instructions[10]:
  #   break

print(abs(position[0]) + abs(position[1]))
