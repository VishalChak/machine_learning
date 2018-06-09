def selection_sort(arr):
    for i in range(len(arr)):
        indx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[indx]:
                indx = j
        arr[i], arr[indx] = arr[indx], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key< arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr
def merge(arr, left, m, right)

def merge_sort(arr, left , right):
    if right > left:
        m = (left+right)//2
        merge_sort(arr, left,m)
        merge_sort(arr, m+1, right)
        



if __name__ == "__main__":
    arr = [45,2,3,0,23,6,7]
    #print(selection_sort(arr))
    #print(bubble_sort(arr))
    #print(insertion_sort(arr))
    print(insertion_sort(arr))
    