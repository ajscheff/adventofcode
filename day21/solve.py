import itertools

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

alle_to_ingreds = {}
ingred_lists = []
alle_lists = []
ingred_possibly_has = {}
for line in lines:
  parts = line.split(" (contains ")
  ingreds = parts[0].split(" ")
  ingred_lists.append(ingreds)
  alls = parts[1][:-1].split(", ")
  alle_lists.append(alls)
  for alle in alls:
    if alle not in alle_to_ingreds:
      alle_to_ingreds[alle] = []
    alle_to_ingreds[alle].append(set(ingreds))

  for ingred in ingreds:
    if ingred not in ingred_possibly_has:
      ingred_possibly_has[ingred] = set()

    for alle in alls:
      ingred_possibly_has[ingred].add(alle)


does_not_have = {}


def many_set_intersection(sets):
  intersection_set = set(sets[0])
  for s in sets:
    intersection_set = intersection_set.intersection(s)
  return intersection_set


for alle in alle_to_ingreds:
  ingred_sets = alle_to_ingreds[alle]
  intersection_set = many_set_intersection(ingred_sets)

  does_not_have[alle] = set()
  for ingred_set in ingred_sets:
    for ingred in ingred_set:
      if ingred not in intersection_set:
        does_not_have[alle].add(ingred)

alle_free = set()
for ingred in ingred_possibly_has:
  possible_alles = ingred_possibly_has[ingred]
  may_have = False
  for alle in possible_alles:
    if ingred not in does_not_have[alle]:
      may_have = True
      break

  if not may_have:
    alle_free.add(ingred)


count = 0
for ingred_list in ingred_lists:
  for ingred in ingred_list:
    if ingred in alle_free:
      count += 1

all_ingreds = set()
for ingred_list in ingred_lists:
  possible_alle = filter(lambda x: x not in alle_free, ingred_list)
  print(possible_alle)
  for poss in possible_alle:
    print(poss)
    all_ingreds.add(poss)


cand_ingreds = list(all_ingreds)
all_alles = alle_to_ingreds.keys()

print cand_ingreds
print all_alles

rem_ingreds_lists = []
for ingred_list in ingred_lists:
  filtered = filter(lambda i: i not in alle_free, ingred_list)
  rem_ingreds_lists.append(filtered)


def check_row(allergens, inlist, allist):
  included_alles = map(lambda x: allergens[x], inlist)
  return set(allist).issubset(set(included_alles))


def check_perm(perm):
  allergens = dict(zip(perm, all_alles))
  for i in range(len(rem_ingreds_lists)):
    inlist = rem_ingreds_lists[i]
    allist = alle_lists[i]
    if not check_row(allergens, inlist, allist):
      return False
  return True


for perm in itertools.permutations(cand_ingreds):
  if check_perm(perm):
    print(dict(zip(perm, all_alles)))
