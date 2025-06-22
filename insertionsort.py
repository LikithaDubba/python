def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=1-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=list(map(int,input("enter numbers separated by space:").split()))
insertion(arr)
print(arr)
