def ReverseTheRange(arr,start,end):
    i=start
    j=end
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
arr=list(map(int,input().split()))
start=int(input())
end=int(input())
print(ReverseTheRange(arr,start,end))