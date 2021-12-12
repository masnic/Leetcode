def twoSum(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                res.append(i)
                res.append(j)
                break
    return res
