def sum_p(n):
    p={2,3,5,7}
    t=0
    if n==0:
        return 0
    while n>0:
        d=n%10
        if d in p:
            t+=d
        n=n//10
    return t
n=236
print(sum_p(n))