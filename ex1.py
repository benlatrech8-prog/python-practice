def total(nums):
 resualt=0
 for i in range(len(nums)):
 	resualt=resualt+nums[i]
 return resualt

print(total([1,2,3]))
print(total([10,-5,5]))
print(total([]))
