def bubble_sort(nums):
	for i in xrange(len(nums)-1):
		for j in xrange(len(nums)-i):
			if nums[i] > nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]

foo = [1,3,2,6,4,9,7]
bubble_sort(foo)
print foo