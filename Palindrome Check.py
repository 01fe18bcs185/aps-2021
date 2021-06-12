# Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

def isPalindrome(strs):
    l = 0
	r = len(strs) - 1
	while l < r:
		if strs[l] != strs[r]:
			return False
		l += 1
		r -= 1
	return True
