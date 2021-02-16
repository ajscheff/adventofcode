input_file = open('p1input.txt', 'r')
lines = input_file.readlines()

numbers = []
for line in lines:
  numbers.append(int(line.strip()))

for n in numbers:
  for m in numbers:
    for o in numbers:
      if n + m + o == 2020:
        print(str(n) + " " + str(m) + " " + str(o))
