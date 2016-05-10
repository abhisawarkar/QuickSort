#!/bin/python

def quicksort(arr,low,high):
	if low < high:
		pivot=partition(arr,low,high)
		quicksort(arr,low,pivot-1)
		quicksort(arr,pivot+1,high)


def partition(arr,low,high):
	wall = low-1
    	pivot = arr[high]     
    	for j in range(low , high):
        	if   arr[j] <= pivot:
        	    wall += 1
        	    arr[wall],arr[j] = arr[j],arr[wall]
 
    	arr[wall+1],arr[high] = arr[high],arr[wall+1]
	return ( wall+1 )


L=[10,9,8,7,6,5,4,3,2,1]
quicksort(L,0,len(L)-1)
print L
