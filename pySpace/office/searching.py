def linear_search(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1

def binary_search(arr,x,left, right):
    if left <= right:
        m = (left+right)//2
        if arr[m] == x:
            return m
        elif arr[m] < x:
            return binary_search(arr,x,m+1, right)
        elif arr[m] > x:
            return binary_search(arr,x,left, m-1)
    else:
        return -1
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print(linear_search(arr, 10))
    print(binary_search(arr,6,0,len(arr)))