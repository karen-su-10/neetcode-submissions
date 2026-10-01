class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap, key as the sorted string, value as the array
        dic = dict()
        # loop through the strs, put in the hashmap
        for i in strs:
            sorted_i = str(sorted(i))
            if sorted_i in dic:
                dic[sorted_i].append(i)
            else:
                dic[sorted_i] = [i]
            
        # loop through the hashmap, get values and add to the array
        output =[]
        for i in dic:
            output.append(dic[i])
        return output
