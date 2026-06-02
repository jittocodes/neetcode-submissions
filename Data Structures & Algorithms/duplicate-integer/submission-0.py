class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        app = set()

        for i in nums:
            if i in app:
                return True
            else:
                app.add(i)
    
        return False
