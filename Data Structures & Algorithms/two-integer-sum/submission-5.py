class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #val-> index

        for index,num in enumerate(nums):
            indices[num] = index
        
        for curr_index,n in enumerate(nums):
            diff = target - n

            if diff in indices.keys() and indices[diff] != curr_index:
                return [curr_index, indices[diff]]
        return []
            