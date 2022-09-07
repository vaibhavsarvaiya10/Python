
import re


class Solution:
    def twoSum(self, nums, target):
        req = []
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                adtn = nums[i] + nums[j]
                if adtn == target:
                    if i != j:
                        req.append(i)
                        req.append(j)
                        return req


var1 = int(input("Enter limit : "))
inp = []
for i in range(var1):
    a = int(input("Enter the value : "))
    inp.append(a)

print(inp)
var2 = int(input("Enter the target : "))

val = Solution()
print(val.twoSum(inp, var2))
