input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

first_break = lines.index("")
rule_lines = lines[:first_break]
my_ticket_line = lines[first_break+2]
ticket_lines = lines[first_break+5:]


def parse_rules(rule_lines):
  rules = {}
  for line in rule_lines:
    parts = line.split(": ")
    range_strs = parts[1].split(" or ")
    ranges = []
    for range_str in range_strs:
      range_parts = range_str.split("-")
      ranges.append(range(int(range_parts[0]), int(range_parts[1]) + 1))

    rules[parts[0]] = ranges

  return rules


rules = parse_rules(rule_lines)


def valid_field_rule(val, rule):
  for r in rules[rule]:
    if val in r:
      return True
  return False


def valid_field(val, rules):
  for ranges in rules.values():
    for r in ranges:
      if val in r:
        return True
  return False


def valid_line(line, rules):
  for val_str in line.split(","):
    val = int(val_str)
    if not valid_field(val, rules):
      return False
  return True


valid_ticket_lines = filter(lambda x: valid_line(x, rules), ticket_lines)
valid_tickets = list(map(lambda x: x.split(","), valid_ticket_lines))

possibilities = [rules.keys()
                 for i in range(len(valid_tickets[0]))]

for item in range(len(valid_tickets[0])):
  for ticket in range(len(valid_tickets)):
    val = valid_tickets[ticket][item]
    possibilities[item] = filter(
        lambda rule: valid_field_rule(int(val), rule), possibilities[item])


determined = filter(lambda x: len(x) <= 3, possibilities)

undetermined = filter(lambda x: len(x) > 2, possibilities)

final = ["" for i in range(len(possibilities))]

while True:
  for i in range(len(possibilities)):
    if len(possibilities[i]) == 1:
      found = possibilities[i][0]
      final[i] = found
      for j in range(len(possibilities)):
        if found in possibilities[j]:
          possibilities[j].remove(found)
      break

  if len(filter(lambda x: x == "", final)) == 0:
    break

my_ticket = my_ticket_line.split(",")

prod = 1
for i in range(len(my_ticket)):
  if final[i][:9] == "departure":
    prod = prod * int(my_ticket[i])

print(prod)
