nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    # Iterate i 
    for i in range(len(nums)):
        for j in range(len(nums)-1): 
            if nums[i] + nums[j] == target:
                return i, j    

if __name__ == "__main__":
    print(*two_sum(nums, target))