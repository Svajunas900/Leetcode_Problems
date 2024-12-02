
def twoSum(nums, target):
    a_dict = {}
    for i, n in enumerate(nums):
        if target-n in a_dict:
            return [i, a_dict[target-n]]
        a_dict[n] = i
            
    return 0
