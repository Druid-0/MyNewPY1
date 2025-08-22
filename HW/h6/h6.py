

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # Начинаем с i+1, чтобы избежать использования одного элемента дважды
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Если решение не найдено
