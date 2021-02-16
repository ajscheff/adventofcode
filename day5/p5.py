input_file = open('p5input.txt', 'r')
lines = input_file.readlines()


def generic_number(input_str, lower_symbol, upper_symbol):
  bottom_rang = 0
  top_rang = 2 ** len(input_str)
  for c in input_str:
    middle = (top_rang + bottom_rang) / 2
    if c == lower_symbol:
      top_rang = middle
    elif c == upper_symbol:
      bottom_rang = middle

  return bottom_rang


def col_number(col_str):
  return generic_number(col_str, "L", "R")


def row_number(row_str):
  return generic_number(row_str, "F", "B")


all_seats = []
for line in lines:
  row_part = line[:7]
  col_part = line[7:].strip()

  row_num = row_number(row_part)
  col_num = col_number(col_part)

  seat_id = row_num * 8 + col_num
  all_seats.append(seat_id)


all_seats.sort()
for i in range(len(all_seats)-1):
  seat = all_seats[i]
  next_seat = all_seats[i+1]
  if next_seat - seat == 2:
    print((seat + next_seat) / 2)
