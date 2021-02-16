input_file = open('p9input.txt', 'r')
lines = input_file.readlines()
nums = [int(line.strip()) for line in lines]


def check(prev_list, target):
  for i in range(len(prev_list)):
    for j in range(i+1, len(prev_list)):
      if prev_list[i] + prev_list[j] == target:
        return True
  return False


target = 0
for i in range(25, len(nums)):
  if not check(nums[i-25:i], nums[i]):
    target = nums[i]
    break

print("target", target)

for i in range(len(nums)):
  sum = 0
  j = i
  found = False
  while sum < target and j < len(nums):
    sum += nums[j]
    j += 1
    if sum == target:
      found = True
      sub_list = nums[i:j]
      print(max(sub_list) + min(sub_list))

  if found:
    break
