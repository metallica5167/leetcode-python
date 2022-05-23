#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
nums=[2,7,11,15]
target=9
hashmap={}
for i,n in enumerate(nums):
    d=target-n
    if d in hashmap:
        #return [hashmap[d],i]
        print([hashmap[d],i])
    else:
        hashmap[n]=i