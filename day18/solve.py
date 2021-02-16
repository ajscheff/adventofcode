input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [list(line.strip().replace(" ", "")) for line in lines]


def find_corr_ind(line, index):
  paren_count = 1
  for i in range(index+1, len(line)):
    if line[i] == "(":
      return -1
    elif line[i] == ")":
      return i
  
  print("something wrong", line, index)

# def solve_no_parens(line):
#   if len(line) == 0:
#     return int(line)
#   val = int(line[0])
#   i = 1
#   while i < len(line):
#     op = line[i]
#     next_val = int(line[i+1])
#     if op == "+":
#       val = val + next_val
#     elif op == "*":
#       val = val * next_val
#     i += 2
#   return val

def solve_no_parens(line):
  try:
    line.index("+")
    line.index("*")
    plus_inds = [[]]
    for i in range(1, len(line), 2):
      if line[i] == '+':
        plus_inds[-1].append(i)
      elif len(plus_inds[-1]) > 0:
        plus_inds.append([])
    
    if len(plus_inds[-1]) == 0:
      plus_inds.pop()
    print(plus_inds)

    for j in range(len(plus_inds)):
      plus_r = plus_inds[len(plus_inds) - j - 1]
      line.insert(plus_r[-1] + 2, ")")
      line.insert(plus_r[0] - 1, "(")
    return solve(line)
  except ValueError:
    val = int(line[0])
    i = 1
    while i < len(line):
      op = line[i]
      next_val = int(line[i+1])
      if op == "+":
        val = val + next_val
      elif op == "*":
        val = val * next_val
      i += 2
    return val


def solve(line):
  try:
    while True:
      line.index("(")
      for i in range(len(line)):
        if line[i] == "(":
          corr_ind = find_corr_ind(line, i)
          if corr_ind > i:
            line = line[:i] + [str(solve_no_parens(line[i + 1:corr_ind]))] + line[corr_ind + 1:]
            break
  except ValueError:
    return solve_no_parens(line)
    print("HERE")


sum = 0
for line in lines:
  sum += solve(line)

print(sum)