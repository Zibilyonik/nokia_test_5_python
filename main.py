def solution(A, B):
    fragments = []
    positions = []
    if A == B:
        return len(A) * (len(A) + 1) // 2
    for i in range(len(A)):
        for j in range(len(A[i:])):
            if sorted(A[i:i+j+1]) == sorted(B[i:i+j+1]):
                fragments.append(A[i:i+j+1])
                positions.append(i)
    return len(fragments)
    