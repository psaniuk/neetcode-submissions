import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounterPairs = Counter(nums)
        
        countersList = []
        for key in numCounterPairs:
            countersList.append([numCounterPairs[key], key])

        largetsValueNumPairs = heapq.nlargest(k, countersList)
        return [keyValue[1] for keyValue in largetsValueNumPairs]
        

