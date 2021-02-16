input_file = open('p4input.txt', 'r')
lines = input_file.readlines()

required_codes = ["ecl", "pid", "eyr", "hcl",
                  "byr", "iyr", "hgt"]  # "cid" optional


def parse_docs():

  docs = [[]]
  for line in lines:
    if line == "\n":
      docs.append([])
    else:
      pairs = line.strip().split(" ")
      for pair in pairs:
        docs[-1].append(pair.split(":"))

  return docs


def validateHgt(heightStr):
  unit = heightStr[-2:]
  amt = int(heightStr[:-2])
  if unit == "cm":
    return amt >= 150 and amt <= 193
  elif unit == "in":
    return amt >= 59 and amt <= 76
  return False


def validateHcl(hclStr):
  if len(hclStr) is not 7:
    return False
  if hclStr[0] is not "#":
    return False

  valid = set("0123456789abcdef")
  for i in range(1, 7):
    if hclStr[i] not in valid:
      return False

  return True


def validatePid(pidStr):
  if len(pidStr) is not 9:
    return False

  valid = set("0123456789")
  for c in pidStr:
    if c not in valid:
      return False

  return True


rules = {'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
         'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
         'eyr': lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
         'hgt': lambda x: validateHgt(x),
         'hcl': lambda x: validateHcl(x),
         'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
         'pid': lambda x: validatePid(x),
         'cid': lambda x: True}


def check_doc(doc):
  print(doc)
  codes = map(lambda x: x[0], doc)
  for code in required_codes:
    if code not in codes:
      print("false code not in codes", code)
      return False

  for pair in doc:
    if not rules[pair[0]](pair[1]):
      print("false rule failed", pair)
      return False

  print("true")
  return True


print(len(filter(lambda x: x, map(check_doc, parse_docs()))))
