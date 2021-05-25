# Input: F
# Output: f

def UpperToLower(char):
	return chr(ord(char) | 32)

print(UpperToLower('F'))