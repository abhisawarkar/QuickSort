#!/bin/python

def quicksort(arr,low,high):
	if low < high:
		pivot=partition(arr,low,high)		# final pivot position after reordering
		quicksort(arr,low,pivot-1)		# sort left side 
		quicksort(arr,pivot+1,high)		# sort right side


def partition(arr,low,high):
	wall = low-1
    	pivot = arr[high]     
    	for j in range(low , high):
        	if   arr[j] <= pivot:
        	    wall += 1
        	    arr[wall],arr[j] = arr[j],arr[wall] # Re-arrange smaller elements to left of pivot and move wall
 
    	arr[wall+1],arr[high] = arr[high],arr[wall+1]	# Swap pivot to beginning of wall 
	return ( wall+1 )
