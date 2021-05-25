# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & # "bbebi".

strs = "cbbebi"
k = 3

res = 0
window_start = 0
s = set()

for window_end in range(len(strs)):
	s.add(strs[window_end])

	while len(s) > k:
		if strs[window_start] in s:
			s.remove(strs[window_start])
		window_start += 1
	res = max(res, window_end - window_start + 1)

print(res)
