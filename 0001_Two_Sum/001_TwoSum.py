class Solution(object):
    def two_sum(self, nums,target):
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic :
                return[dict[complement], i]

            dict[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().two_sum(nums, target) == [0, 1])
    nums = [3, 2, 4]
    target = 6
    assert (Solution().two_sum(nums, target) == [1, 2])
