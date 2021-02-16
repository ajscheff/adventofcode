input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

split = lines.index("")
rule_lines = lines[:split]
input_lines = lines[split+1:]

max_len = max(map(lambda x: len(x), input_lines))

print(max_len)

rules = {}
for line in rule_lines:
  parts = line.split(": ")
  key = parts[0]
  if parts[1][0] == '"':
    rules[key] = {"t": "letter", "v": parts[1][1]}
  else:
    dest_parts = parts[1].split(" | ")
    dests = []
    for dest in dest_parts:
      dests.append(dest.split(" "))
    rules[key] = {"t": "rule", "v": dests}


def get_key(rid, depth):
  return rid + "," + str(depth)


def substr_of_any(s, offset):
  for line in input_lines:
    if offset < len(line):
      if line[offset:][:len(s)] == s >= 0:
        return True
  return False


def evaluate_rule(rid, solutions, starting=0):
  print("==================", rid, starting)
  rule = rules[rid]
  key = get_key(rid, starting)
  print("rule is:", rule)

  if key in solutions:
    print(rid, "using cached sol", len(solutions[key]))
    return solutions[key]

  if rule["t"] == "letter":
    print(rid, "letter")
    return [rule["v"]]
  else:
    results = set()
    for rule_list in rule["v"]:
      inner_results = evaluate_rule(rule_list[0], solutions, starting)
      inner_results = filter(lambda x: substr_of_any(x, starting), inner_results)

      for i in range(1, len(rule_list)):
        new_inreses = set()
        for inres in inner_results:
          inner_inner_reses = evaluate_rule(
              rule_list[i], solutions, starting + len(inres))
          for ininres in inner_inner_reses:
            fullres = inres + ininres
            if substr_of_any(fullres, starting):
              new_inreses.add(fullres)
        inner_results = new_inreses

      for res in inner_results:
        results.add(res)

    print(rid, "caching")
    solutions[key] = results
    print("returning", len(results))
    return results


solutions = {}
res = evaluate_rule("0", solutions)

# for r in res:
#   print(len(r), r)

count = 0
for line in input_lines:
  if line in res:
    count += 1

print(count)
