# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(0, len(A), 2):
        try:
            if A[i] != A[i + 1]:
                return A[i]
        except:
            return A[i]

print(solution([9, 3, 9, 3, 9, 7, 7]))
