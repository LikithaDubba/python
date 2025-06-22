def selection(arr):
    n=len(arr)
    for i in range(n):
        lower=i
        for j in range(i+1,n):
            if arr[j]<arr[lower]:
                lower=j
        arr[i],arr[lower]=arr[lower],arr[i]
arr=[5,4,3,2,1]
selection(arr)
print(arr)