nums = []
for items in range(11):
  nums.append(items)
print(nums)
print(len(nums))
while len(nums) > 0:
  rm = int(input("Which index item to remove?: "))
  if rm > len(nums):
    print("Invalid entry")
    print(nums)
    print(len(nums))
  else:
    if rm == 0:
      print("Invalid entry")
      print(nums)
      print(len(nums))
    else:
      del nums[rm-1]
      if len(nums) == 0:
        for items in range(11):
          nums.append(items)
      print(nums)
      print(len(nums))
