class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        ans = list()
        for i, num in enumerate(numbers):
            need = target - num
            if need in m.keys():
                ans.append(m[need] + 1)
                ans.append(i + 1)

                return ans
            else:
                m[num] = i
        
        return []
        