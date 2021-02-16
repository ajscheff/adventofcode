input_file = open('p10input.txt', 'r')
lines = input_file.readlines()
nums = [int(line.strip()) for line in lines]
nums.sort()
nums.insert(0, 0)
nums.append(nums[-1] + 3)

# ones = 1
# twos = 0
# threes = 1
# for i in range(len(nums) - 1):
#   diff = nums[i+1] - nums[i]
#   if diff == 1:
#     ones += 1
#   elif diff == 2:
#     twos += 1
#   elif diff == 3:
#     threes += 1
#   else:
#     print("unexpected")

# print(ones, twos, threes)
# print(ones * threes)

cache = {}


def num_options(adapters):
  if len(adapters) in cache:
    return cache[len(adapters)]

  if len(adapters) <= 2:
    return 1

  count = 0
  count += num_options(adapters[1:])
  if adapters[2] - adapters[0] <= 3:
    count += num_options(adapters[2:])
  if len(adapters) > 3 and adapters[3] - adapters[0] <= 3:
    count += num_options(adapters[3:])

  cache[len(adapters)] = count
  return count


print(num_options(nums))
