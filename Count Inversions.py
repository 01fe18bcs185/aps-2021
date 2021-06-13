# An inversion occurs if for any valid indices i and j, i < j and A[i] > A[j].

# For example, given A = [3, 4, 1, 2], there are 4 inversions. The following pairs of indices represent inversions: [0, 2], [0, 3], [1, 2], [1, 3].

def countInversions(A):
    return countSubAInversions(A, 0, len(A))

def countSubAInversions(A, start, end):
    if end - start <= 1:
        return 0

    middle = start + (end - start) // 2
    leftInv = countSubAInversions(A, start, middle)
    rightInv = countSubAInversions(A, middle, end)
    mergedInv = mergeSortAndCountInversions(A, start, middle, end)
    return leftInv + rightInv + mergedInv

def mergeSortAndCountInversions(A, start, middle, end):
    sortedA = []
    left = start
    right = middle
    inversions = 0

    while left < middle and right < end:
        if A[left] <= A[right]:
            sortedA.append(A[left])
            left += 1
        else:
            inversions += middle - left
            sortedA.append(A[right])
            right += 1

    sortedA += A[left:middle] + A[right:end]
    for idx, num in enumerate(sortedA):
        A[start + idx] = num

    return inversions
