class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            p = (l + r) // 2
            if nums[p] == target:
                return p

            # Left half is sorted
            if nums[l] <= nums[p]:
                if nums[l] <= target < nums[p]:
                    r = p - 1
                else:
                    l = p + 1
            # Right half is sorted
            else:
                if nums[p] < target <= nums[r]:
                    l = p + 1
                else:
                    r = p - 1

        return -1