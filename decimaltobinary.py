def dtob(n):
    res=""
    while (n!=0):
        rem=n%2
        if rem==1:
            res+="1"
        else:
            res+="0"
        n=n//2
    return res[::-1]
n=7
print(dtob(n))