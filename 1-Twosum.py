nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(len(nums)-1):
        if i + j == target:
            print(i, j)
        