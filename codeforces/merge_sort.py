#Best Case Complexity: O(n*log n)
#Worst Case Complexity: O(n*log n)
#Average Case Complexity: O(n*log n)

def merge_sort(unsorted_array):
    if len(unsorted_array)>1:
        r=len(unsorted_array)//2
        L=unsorted_array[:r]
        R=unsorted_array[r:]

        #solve the two sub half
        merge_sort(L)
        merge_sort(R)
        i=j=k=0

        while i != len(L) and j != len(R):
            if L[i]<R[j]:
                unsorted_array[k]=L[i]
                i=i+1
            else:
                unsorted_array[k]=R[j]
                j=j+1
            k=k+1
        
        while i < len(L):
            unsorted_array[k]=L[i]
            i=i+1
            k=k+1
        while j < len(R):
            unsorted_array[k]=R[j]
            j=j+1
            k=k+1

        return unsorted_array
    else:
        return unsorted_array

if __name__=='__main__':
    arr=[6,5,8,7,3,11,6,33,-1,44,3,-2,-14]
    print(merge_sort(arr))

