
def parse_line(line):
  components = line.split(":")

  pw = components[1].strip()

  requirements = components[0].split(" ")
  requirement_char = requirements[1]

  requirement_range_strs = requirements[0].split("-")
  requirement_range = list(map(lambda x: int(x), requirement_range_strs))

  return requirement_range, requirement_char, pw


def check_parsed(req_range, req_char, pw):
  count_char = 0
  for c in pw:
    if c == req_char:
      count_char += 1

  return count_char >= req_range[0] and count_char <= req_range[1]


def check_parsed_new(req_range, req_char, pw):
  count_char = 0
  for i in req_range:
    if pw[i-1] == req_char:
      count_char += 1
  return count_char == 1


input_file = open('p2input.txt', 'r')
lines = input_file.readlines()


count_valid = 0
for line in lines:
  requirement_range, requirement_char, pw = parse_line(line)
  if check_parsed_new(requirement_range, requirement_char, pw):
    count_valid += 1
  else:
    print("invalid")
    print(line)

print(count_valid)
