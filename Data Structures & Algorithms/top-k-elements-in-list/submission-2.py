class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = dict()
        # loop through the list, put i in hashmap as key, everytime +1
        for i in nums:
            counter_map[i]=counter_map.get(i,0) +1
        #  sort the hashmap by its value desc, and return the ones until k
        sorted_map = sorted(counter_map.keys(), key=lambda x:counter_map[x], reverse=True)
        return sorted_map[:k]
        