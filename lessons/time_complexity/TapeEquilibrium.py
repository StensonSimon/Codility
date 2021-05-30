# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random
def solution(A):
    # write your code in Python 3.6
    c =9999999
    sum1 = sum(A)
    sum2 = 0
    while len(A)>1:
        last_el = A.pop()
        sum2 = sum2 + last_el
        sum1 = sum1-last_el
        diff = abs(sum1-sum2)
        c = min(c,diff)
    return c
    pass

