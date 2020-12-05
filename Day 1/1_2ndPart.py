def solve():
    nums = []
    with open('1.txt') as f:
        for line in f:
            nums.append(int(line.strip()))

    for index, value in enumerate(nums):
        for j in nums[index+1:]:
            for k in nums[index+2:]:
                if value+j+k == 2020:
                    return value*j*k


print(solve())
