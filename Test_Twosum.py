from twosum import two_sum

def test_1two_sum():
    nums = [2,7,11,15]
    target = 9
    assert two_sum(nums, target) == (0, 1)