input_file = open('p6input.txt', 'r')
lines = input_file.readlines()


def parse_docs():
  docs = [[]]
  for line in lines:
    if line == "\n":
      docs.append([])
    else:
      yesses = line.strip()
      docs[-1].append(set(yesses))
  return docs


count = 0
family_set_lists = parse_docs()
# for c in yes_sets[0]:
#   in_all = True
#   for s in yes_sets:
#     if c not in s:
#       in_all = False
#       break

total_count = 0
for fam_set_list in family_set_lists:
  for c in fam_set_list[0]:
    in_all = True
    for s in fam_set_list:
      if c not in s:
        in_all = False
        break

    if in_all:
      total_count += 1

print(total_count)
