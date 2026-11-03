def average(nums):
	
	if len(nums)==0:	
		return 0
	else:
		return sum(nums)/len(nums)
	
print(average([10,20,30]))
print(average([5,6])) 
print(average([]))
