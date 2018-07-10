def merge_sort(start, end, nums):
	if start > end:
		return
	if start == end:
		return nums[start]

	mid = (start + end) / 2
	merge_sort(start, mid, nums)
	merge_sort(mid+1, end, nums)
	merge(start, end, mid, nums)

def merge(start, end, mid, nums):
	temp = [0] * (end-start+1)
	index1 = start
	index2 = mid+1
	list1_size = mid
	index = 0
	while index1 <= list1_size and index2 <= end:
		if nums[index1] <= nums[index2]:
			temp[index] = nums[index1]
			index1 += 1
		else:
			temp[index] = nums[index2]
			index2 += 1
		index += 1

	while index1 <= list1_size:
		temp[index] = nums[index1]
		index1 += 1
		index += 1 

	while index2 <= end:
		temp[index] = nums[index2]
		index2 += 1
		index += 1

	for i in range(start, end+1):
		nums[i] = temp[i-start]

def sort(nums):
	return merge_sort(0, len(nums)-1, nums)

foo = [1,3,2,5,4,9,7,12]
sort(foo)
print foo
