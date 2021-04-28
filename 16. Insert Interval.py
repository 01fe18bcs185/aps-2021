# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7]

a = [[1,3], [5,7], [8,12]]
interval = [4,10]

a = a+[interval]
a.sort()
res = [a[0]]

for i in a:
  prev_end = res[-1][1]
  start = i[0]
  end = i[1]

  if start <= prev_end:
    res[-1][1] = max(prev_end, end)
  else:
    res.append(i)
    
print(res) 
