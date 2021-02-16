input_file = open('p7input.txt', 'r')
lines = input_file.readlines()


contained_by = {}
contains = {}


def parse_line(line):
  parts = line.split(" bags contain ")
  color = parts[0]

  contained_list = []
  if parts[1] != "no other bags.":
    contained_list = parts[1].split(", ")
    contained_list = map(
        lambda x: [x[:x.index(" ")], x[(x.index(" ")+1):x.rindex(" ")]], contained_list)
    contained_by[color] = contained_list

  for contained in contained_list:
    contained_color = contained[1]
    if contained_color not in contains:
      contains[contained_color] = []
    contains[contained_color].append(color)


for line in lines:
  parse_line(line.strip())

visited = set()


def traverseContains(color, first=False):
  if color in visited:
    return

  if not first:
    visited.add(color)
  if color in contains:
    for container in contains[color]:
      traverseContains(container)


# traverseContains("shiny gold", True)
def traverseContainedBy(color, first=False):
  if color not in contained_by:
    return 1

  contained_list = contained_by[color]
  total = 0 if first else 1
  for contained in contained_list:
    total += int(contained[0]) * traverseContainedBy(contained[1])
  return total


# print(contained_by)
print(traverseContainedBy("shiny gold", True))
