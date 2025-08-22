
        # n1 [2, 7, 11, 15]
        # n2 = target
        # n2 = target - n1
        # for i in range(n1):
        #   for j in (i - n2):
        #       if i == target:
        #           return j

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:

                    return [i, j]
        # if not found
        print("not found")
        return []

exmpl = Solution()
print(exmpl.twoSum([2, 7, 3, 5, 11, 15], 19))
