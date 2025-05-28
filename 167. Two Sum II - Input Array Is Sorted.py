class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        while first < last:
            summation = numbers[first] + numbers[last]
            if summation == target:
                return [first + 1, last + 1]
            elif summation > target:
                last -= 1
            else:
                first += 1
        return []

        