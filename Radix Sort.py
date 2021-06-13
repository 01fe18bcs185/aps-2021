def radixSort(A):
    if len(A) == 0:
        return A

    maxNumber = max(A)
    digit = 0

    while maxNumber / 10 ** digit > 0:
        countingSort(A, digit)
        digit += 1

    return A

def countingSort(A, digit):
    sortedA = [0] * len(A)
    countA = [0] * 10
    digitColumn = 10 ** digit

    for num in A:
        countIndex = (num // digitColumn) % 10
        countA[countIndex] += 1

    for i in range(1, 10):
        countA[i] += countA[i - 1]

    for i in range(len(A) - 1, -1, -1):
        countIndex = (A[i] // digitColumn) % 10
        countA[countIndex] -= 1
        sortedIndex = countA[countIndex]
        sortedA[sortedIndex] = A[i]

    for i in range(len(A)):
        A[i] = sortedA[i]
