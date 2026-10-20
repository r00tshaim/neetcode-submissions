class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for index in range(len(arr)-1, -1, -1):
            last_max = right_max
            if arr[index] > right_max:
                right_max = arr[index]

            if index == len(arr)-1:
                arr[index] = -1
            else:
                arr[index] = last_max
        return arr
        