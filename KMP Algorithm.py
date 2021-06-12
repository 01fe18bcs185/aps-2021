# Write a function that takes in two strings and checks if the first string contains the second one using the Knuth—Morris—Pratt algorithm. The function should return a boolean.

def knuthMorrisPrattAlgorithm(string, substring):
    pattern = build_pattern(substring)
	return does_match(string, substring, pattern)
	
def build_pattern(substring):
	pattern = [-1 for _ in substring]
	j = 0
	
	for i, char in enumerate(substring[1:], 1):
		if char == substring[j]:
			pattern[i] = j
			j += 1
		else:
			if j > 0: #if we've got a pattern
				j = pattern[j - 1] + 1
			
	return pattern

def does_match(string, substring, pattern):
	i = 0
	j = 0
	
	while i + len(substring) - j <= len(string):
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
			
	return False
