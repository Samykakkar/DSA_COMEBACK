class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first(nums, target):
            low = 0
            high = len(nums) - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    first = mid
                    high = mid - 1

                if nums[mid] < target:
                    low = mid + 1
                if nums[mid] > target:
                    high = mid - 1
            return first

        def last(nums, target):
            low = 0
            high = len(nums) - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    last = mid
                    low = mid + 1

                if nums[mid] < target:
                    low = mid + 1
                if nums[mid] > target:
                    high = mid - 1
            return last

        first = first(nums, target)
        last = last(nums, target)

        return [first, last]
