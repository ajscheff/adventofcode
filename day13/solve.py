from fractions import gcd
input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]


target = int(lines[0])
# bus_nos = list(map(lambda x: int(x), filter(
#     lambda x: x != "x",  lines[1].split(","))))
bus_nos = lines[1].split(",")

bwd = []
for i in range(len(bus_nos)):
  if bus_nos[i] != 'x':
    bwd.append([int(bus_nos[i]), i])

print(bwd)


def lcm(x, y):
  return x * y // gcd(x, y)


def computet(freq, offset, next_freq, next_offset):
  k = 0
  val = offset
  while (val + next_offset) % next_freq != 0:
    k += 1
    val += freq
  return val


current = bwd.pop(0)
next = bwd.pop(0)

while len(bwd) > 0:
  res = computet(current[0], current[1], next[0], next[1])
  current = [lcm(current[0], next[0]), res]
  next = bwd.pop(0)
  res = computet(current[0], current[1], next[0], next[1])
  print(res)


# def wait_time(bus_no, target):
#   next_arrival = ((target / bus_no) + 1) * bus_no
#   return next_arrival - target

# shortest_wait = 1000000
# shortest_wait_bus = 0
# for bus_no in bus_nos:
#   wait = wait_time(bus_no, target)
#   if wait < shortest_wait:
#     shortest_wait = wait
#     shortest_wait_bus = bus_no

# print(shortest_wait_bus * shortest_wait)
