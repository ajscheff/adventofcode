input_file = open('p8input.txt', 'r')
lines = input_file.readlines()
lines = [line.strip() for line in lines]

instructions = [line.split(" ") for line in lines]
instructions = [[ins[0], int(ins[1])] for ins in instructions]


# acc = 0
# fp = 0
# prev_fps = set()

# while fp not in prev_fps:
#   prev_fps.add(fp)
#   ins = instrutions[fp][0]
#   arg = instrutions[fp][1]

#   if ins == "acc":
#     acc += arg
#     fp += 1
#   elif ins == "jmp":
#     fp += arg
#   elif ins == "nop":
#     fp += 1
#   else:
#     print("unrecognized instruction", instrutions[fp])

def run(ins_list, fp=0, acc=0, prev_fps=set()):
  if fp in prev_fps:
    return (acc, True)
  if fp == len(ins_list):
    return (acc, False)

  prev_fps.add(fp)

  ins = ins_list[fp][0]
  arg = ins_list[fp][1]

  if ins == "acc":
    return run(ins_list, fp + 1, acc + arg, prev_fps)
  elif ins == "jmp":
    return run(ins_list, fp + arg, acc, prev_fps)
  elif ins == "nop":
    return run(ins_list, fp + 1, acc, prev_fps)
  else:
    print("unrecognized instruction", ins_list[fp])


for i in range(len(instructions)):
  ins = instructions[i][0]
  if ins == "jmp":
    instructions[i][0] = "nop"
    result = run(instructions, 0, 0, set())
    if not result[1]:
      print(result)
    instructions[i][0] = "jmp"
  elif ins == "nop":
    instructions[i][0] = "jmp"
    result = run(instructions, 0, 0, set())
    if not result[1]:
      print(result)
    instructions[i][0] = "nop"
