def kadane(nums):
    global_max = 0
    cur_max = 0

    for i in range(len(nums)):
    	cur_max += nums[i]
    	cur_max=max(cur_max, 0)
    	global_max = max(global_max, cur_max)

    return global_max
    
print(kadane([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))
