# Input: f
# Output: F

def LowerToUpper(char):
	return chr(ord(char) & ~32)

print(LowerToUpper('f'))