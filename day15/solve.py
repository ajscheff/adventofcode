starting = [2, 0, 1, 9, 5, 19]

curr_turn = 1
said_on = {}
said = []


def say(num):
  global curr_turn
  said.append(num)

  if num not in said_on:
    said_on[num] = []
  said_on[num].append(curr_turn)

  if len(said_on[num]) > 2:
    said_on[num] = said_on[num][-2:]
  curr_turn += 1


for i in range(len(starting)):
  say(starting[i])

while len(said) < 30000000:
  last_said = said[-1]
  if len(said_on[last_said]) == 1:
    say(0)
  else:
    say(said_on[last_said][-1] - said_on[last_said][-2])

  if len(said) % 100000 == 0:
    print(len(said))

print(said[-1])
