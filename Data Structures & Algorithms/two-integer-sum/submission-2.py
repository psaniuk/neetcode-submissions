class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndexPairs = dict()
    
        for i in range(len(nums)):
            first_num = nums[i]
            second_num = target - first_num

            if second_num in valueToIndexPairs:
                return [valueToIndexPairs[second_num], i]

            valueToIndexPairs[first_num] = i

        return []