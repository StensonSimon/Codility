# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    return int((len(A)+1)*(len(A)+2)/2 - sum(A))
    pass


print(solution([2,3,1,5]))