input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

split_index = lines.index("Player 2:")
p1_lines = lines[1:split_index-1]
p2_lines = lines[split_index+1:]

p1 = list(map(lambda x: int(x), p1_lines))
p2 = list(map(lambda x: int(x), p2_lines))

while len(p1) != 0 and len(p2) != 0:
  p1c = p1.pop(0)
  p2c = p2.pop(0)

  if p1c > p2c:
    p1.extend([p1c, p2c])
  else:
    p2.extend([p2c, p1c])

mult = 1
total = 0
for i in range(len(p1)):
  total += mult * p1[len(p1)-1-i]
  mult += 1

print total
