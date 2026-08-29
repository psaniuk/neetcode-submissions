class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # if target < nums[left] and target > nums[right]:
        #     return -1
        

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            
            if nums[middle] >= nums[left]:
                if target >= nums[left] and target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            elif nums[middle] <= nums[right]:
                if target >= nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1


        return -1



