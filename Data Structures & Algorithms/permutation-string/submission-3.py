class Solution:
    def checkInclusion(self, target: str, input_str: str) -> bool:
        if len(target) > len(input_str):
            return False

        if input_str == target:
            return True

        if not input_str or not target:
            return False

        left = 0
        sorted_target = sorted(target)

        for right in range(len(input_str)):   
            sub_str = input_str[left:right + 1]             
            if len(sub_str) == len(target):
                if sorted(sub_str) == sorted_target:
                    return True
                left += 1

        return False









