#No. of Comparisons : 2(N-2) +1 in the worst case

def minMax(arr):
    n = len(arr)
    least = arr[0]
    highest = arr[1]
    
    if least > highest: # one comparision
        temp = least 
        least = highest
        highest = temp
        
    #In the worst if the array is sorted in decreasing order, we will have  2 comparisions for 
    #each of the numbers.
    for i in range(2, n):
        if arr[i] > highest:
            highest = arr[i]
        elif arr[i] < least :
            least = arr[i]
        
    return (highest,least)

#In total 2(N-2) +1 comparisons.

print(minMax([5,4,3,2,1]))
