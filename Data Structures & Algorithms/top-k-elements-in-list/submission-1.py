class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ans = {}

        # for i in nums:
        #     if i in ans.keys():
        #         ans[i] = ans[i] + 1
        #     else:
        #         ans[i] = 1
        
        # print(ans)

        # sorted_items = sorted(ans, key=ans.get, reverse=True)


        # print(sorted_items)
        # ans_list = []
        # for i in range(k):
        #     ans_list.append(sorted_items[i])
        
        # return ans_list

        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            counts[i] = 1 + counts.get(i, 0)
        for n, c in counts.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans