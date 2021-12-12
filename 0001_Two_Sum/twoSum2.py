def twoSum(nums,target):
    dict = {}
    for i in range(len(nums)):
        dict.update({nums[i] : i})  #Generate the dictionary: each elements in [nums] as Key, and index as dictionary value
    for j in range(len(nums)):
        diff = target - nums[j]
        if diff in dict and dict[diff] != j: # Remove the case of one number and its double as target
            return [j, dict[diff]]
        else:
            return -1

        
      
