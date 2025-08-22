


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)
        # n1 [1,2,4,5,7,33]
        # n2 = target
        # n2 = target - n1
        # for i in range(n1):
        #   for j in (i - n2):
        #       if i == target:
        #           return j
        #       else:
        #           print("not found")