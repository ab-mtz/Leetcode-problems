nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    # Iterate trough list. take firts element to compare to
    for i in range(len(nums)):
        # Iterate a second time the list starting with the element after i
        for j in range(i + 1, len(nums)): 
            # check if the sum of values in list with i, j indexes reach the target
            if nums[i] + nums[j] == target:
                # if so, return the indexes
                return i, j    

if __name__ == "__main__":
    print(*two_sum(nums, target))