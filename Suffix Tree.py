# Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be the root node of the trie and should support:

# Creating the trie from a string; this will be done by calling the populateSuffixTrieFrom method upon class instantiation, which should populate the root of the class.
# Searching for strings in the trie.

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			self.insert(i, string)
	
	def insert(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			char = string[j]
			if char not in node:
				node[char] = {}
			node = node[char]
		node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
		for char in string:
			if char not in node:
				return False
			node = node[char]
			
		return self.endSymbol in node
