def heapSort(array):
	heap = MaxHeap(array)
	for end_idx in reversed(range(1, len(array))):
		heap.swap(0, end_idx, array)
		heap.siftDown(0, end_idx - 1, array)
	return array
	
class MaxHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent_idx = (len(array) - 2) // 2
		for cur_idx in reversed(range(first_parent_idx + 1)):
			self.siftDown(cur_idx, len(array) - 1, array)
		return array
		
    def siftDown(self, cur_idx, end_idx, heap):
        child1_idx = cur_idx * 2 + 1
		while child1_idx <= end_idx:
			child2_idx = cur_idx * 2 + 2 if cur_idx * 2 + 2 <= end_idx else -1
			if child2_idx > -1 and heap[child2_idx] > heap[child1_idx]:
				idx_to_swap = child2_idx
			else:
				idx_to_swap = child1_idx
			if heap[idx_to_swap] > heap[cur_idx]:
				self.swap(idx_to_swap, cur_idx, heap)
				cur_idx = idx_to_swap
				child1_idx = cur_idx * 2 + 1
			else:
				return
        
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]


print(heapSort([1,4,5,2,6]))