# Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.

def caesarCipherEncryptor(string, key):
	res = []
	for char in string:
    	char = (ord(char) - 97 + key)%26
		res.append(chr(char + 97))
	return "".join(res)
