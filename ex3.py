def count_even(nums):
	
	s_ev=0
	for n in nums:
		if n % 2 == 0:
			s_ev+=1

	return s_ev 
print(count_even([1,2,3,4,6]))
print(count_even([1,3,5]))
print(count_even([]))
