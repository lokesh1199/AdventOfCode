def solve():
    nums = []
    with open('1.txt') as f:
        for line in f:
            nums.append(int(line.strip()))

    for index, value in enumerate(nums):
        for j in nums[index+1:]:
            if value+j == 2020:
                return value*j


print(solve())
