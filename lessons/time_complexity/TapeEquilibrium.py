# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random
def solution(A):
    # write your code in Python 3.6
    c =9999999
    sum1 = sum(A)-A[-1]
    sum2 = A[-1]

    print(sum1)
    for i in range(1, len(A)):
        c = min(abs(sum1-sum2), c)
        
    return c
    pass

A=[]
for i in range(1,10000):
    A.append(random.randint(0,100))
print(solution([3,1,2,4,3]))