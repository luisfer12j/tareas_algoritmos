
def fibonacci(arr,sum):
    if len(arr) == 0:
        arr.append(1)
        arr.append(2)
    if arr[-1]<4000000:
        arr.append(arr[len(arr)-2] + arr[len(arr)-1])
        fibonacci(arr,0)
    i=0
    while i<len(arr):
        if arr[i]%2 == 0:
            sum = sum + arr[i]
        i+=1
    return sum

list = []
print(fibonacci(list,0))
