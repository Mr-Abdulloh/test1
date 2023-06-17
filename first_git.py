class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sun=0
        for i in range(len(nums)):
            if nums.count(0)==len(nums):
                break
            a=min(list(filter(lambda x:x,nums)))
            sun+=1
            for k in range(len(nums)):
                if nums[k]!=0:
                    nums[k]-=a
        return sun
