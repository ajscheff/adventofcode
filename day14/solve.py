input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]


def unpad(bin_str):
  while bin_str[0] == "0":
    bin_str = bin_str[1:]
  return bin_str


def bin_to_int(bin_str):
  unpadded = unpad(bin_str)
  return int(unpadded, 2)


def binary(number):
  return bin(number)[2:]


def pad(bin, mask):
  pad_amt = len(mask) - len(bin)
  return "".join(["0" for i in range(pad_amt)]) + bin


def combine(bin_number, mask):
  pbd = pad(bin_number, mask)
  result = []
  for i in range(len(mask)):
    b = pbd[i]
    m = mask[i]

    if m == "X":
      result.append(b)
    else:
      result.append(m)

  return "".join(result)


def combine_add(bin_add, mask):
  pba = pad(bin_add, mask)
  result = []
  for i in range(len(mask)):
    a = pba[i]
    m = mask[i]

    if m == "0":
      result.append(a)
    else:
      result.append(m)

  return "".join(result)


def replace(st, i, c):
  ar = list(st)
  ar[i] = c
  return "".join(ar)


def addresses_from_floating(addwfl):
  xind = addwfl.find("X")
  if xind == -1:
    return [addwfl]

  addwfl = replace(addwfl, xind, "0")
  to_ret = addresses_from_floating(addwfl)
  addwfl = replace(addwfl, xind, "1")
  to_ret.extend(addresses_from_floating(addwfl))
  return to_ret


mask = ""
memory = {}

for line in lines:
  parts = line.split(" = ")
  if parts[0] == "mask":
    mask = parts[1]
  else:
    # bin_str = binary(int(parts[1]))

    # to_insert_bin = combine(bin_str, mask)
    # to_insert = bin_to_int(to_insert_bin)

    # index = int(parts[0][4:-1])
    # memory[index] = to_insert

    # print(bin_str)
    # print(mask)
    # print(to_insert_bin)
    # print(to_insert)

    add = int(parts[0][4:-1])
    bin_add = binary(add)
    combined = combine_add(bin_add, mask)

    for final_add in addresses_from_floating(combined):
      memory[final_add] = int(parts[1])

sum = 0
for val in memory.values():
  sum += val

print(sum)
