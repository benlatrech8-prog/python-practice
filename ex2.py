def biggest(nums):
	m=nums[0]
	for n in nums:
		if n>m:
			m=n
	return m
print(biggest([3,9,2]))
print(biggest([-5,-1,-8]))
print(biggest([7]))
