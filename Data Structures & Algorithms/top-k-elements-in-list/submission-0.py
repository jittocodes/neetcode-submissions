class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}

        for i in nums:
            if i in ans.keys():
                ans[i] = ans[i] + 1
            else:
                ans[i] = 1
        
        print(ans)

        sorted_items = sorted(ans, key=ans.get, reverse=True)


        print(sorted_items)
        ans_list = []
        for i in range(k):
            ans_list.append(sorted_items[i])
        
        return ans_list