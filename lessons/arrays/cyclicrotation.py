from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    print(A)
    x = deque(A)
    x.rotate(K)
    print(list(x))
pass




solution([1,2,3,4], 4)