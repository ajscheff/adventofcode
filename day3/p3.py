input_file = open('p3input.txt', 'r')
lines = input_file.readlines()


def compute_for_slope(x_slope, y_slope):
  x = 0
  y = 0

  trees = 0
  while y < len(lines):
    line = lines[y].strip()
    if line[x % len(line)] == "#":
      trees += 1

    x += x_slope
    y += y_slope

  return trees


print(compute_for_slope(1, 1) * compute_for_slope(3, 1) *
      compute_for_slope(5, 1) * compute_for_slope(7, 1) * compute_for_slope(1, 2))
