def contains(nums,target):
	
	for n in nums:
		if target == n:
			return True
	return False
print(contains([4,7,1],7))
print(contains([4,7,1],5))
print(contains([],3))
