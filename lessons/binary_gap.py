def solution(N):
    # write your code in Python 3.6
    count = 0
    s = 0
    flag = 0
    while N > 0:
        if N%2 ==1:
            flag =1
            s = max(count, s)
            count = 0

        elif flag == 1:
            count = count + 1
        N = int(N / 2)
    print(s)
    pass


solution(1041)