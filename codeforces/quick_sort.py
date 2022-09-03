def partiation(array, low, high):
    pivot=array[high]
    
    #pointer for greater element
    i=low-1

    #here compare each element with pivot
    for j in range(low, high):
        if array[j]<=pivot:
            i=i+1
            (array[i], array[j])=(array[j],array[i])
    #swap the pivot with greater element
    (array[i+1],array[high])=(array[high],array[i+1])

    return i+1

def quick_sort(array, low, high):
    if low < high:
        pivot=partiation(array, low, high)
        quick_sort(array, low, pivot-1)
        quick_sort(array, pivot+1,high)

        return array

if __name__=='__main__':
    arr=[3,-1,34,-23,77,11,-3,0,1,22,44,22,3,4,6,8,2]
    size=len(arr)
    print(size)
    print(quick_sort(arr, 0, size-1))
