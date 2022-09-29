import sys

a, p = map(int, sys.stdin.readline().split())
nums = [a]
while True:
    temp_list = list(map(int, list(str(nums[len(nums) - 1]))))
    num = 0
    for temp in temp_list:
        num += temp ** p
    if num in nums:
        answer = nums.index(num)
        break
    else:
        nums.append(num)
    
print(answer)
