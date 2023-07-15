# Imports
import sys
import time
import random


def bubbleSort(numbers):
	# Classic Bubble sort
	# Go through array and swap numbers in the wrong place. Keep looping through until no swaps happen (sorted).
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(numbers) - 1):
			if numbers[i] > numbers[i+1]:
				swapped = True
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
	return numbers


def fasterBubbleSort(numbers):
	# Bubble sort but stopping when you get to the sorted numbers on right side
	swapped = True
	iterations = 0
	while swapped:
		iterations += 1
		swapped = False
		for i in range(len(numbers) - (iterations)):
			if numbers[i] > numbers[i+1]:
				swapped = True
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
	return numbers


def selectionSort(numbers):
	# Loop through array to find smallest number and swap it with the next unsorted element.
	# Finished when the sorted elements size is the array size. 
	n = 0
	while(n < len(numbers)):
		minSize = numbers[n]
		minIndex = n
		# Find next smallest integer
		for i in range(n, len(numbers)):
			if numbers[i] < minSize:
				minSize = numbers[i]
				minIndex = i
		# Swap smallest with the current spot
		numbers[n], numbers[minIndex] = numbers[minIndex], numbers[n]
		n += 1
	return numbers


def insertionSort(numbers):
	# First number goes in sorted array
	sortedNumbers = [numbers.pop()]

	# Keep inserting numbers into sorted array until unsorted is empty
	while(len(numbers) > 0):
		nextNumber = numbers.pop()
		# If the next number doesn't get inserted during the loop, insert it at the end of the sorted array
		inserted = False
		for i in range(len(sortedNumbers)):
			if nextNumber < sortedNumbers[i]:
				sortedNumbers.insert(i, nextNumber)
				inserted = True
				break
		if not inserted:
			sortedNumbers.append(nextNumber)
	return sortedNumbers

def quickSort(numbers):
	# Base case
	if len(numbers) <= 1:
		return numbers

	pivot = numbers[len(numbers) - 1]
	left, right = [],[]

	# Pick a pivot number and place all lower numbers in left, higher numbers in right
	for num in numbers[:-1]:
		if num < pivot:
			left.append(num)
		else:
			right.append(num)

	# Recursion
	return quickSort(left) + pivot + quickSort(right)




def calculateTimeComplexity(func, numbers):
	start = time.time()
	sortedNumbers = func(numbers)
	end = time.time()
	print(f"Finished in {(end - start) * 1000000} microseconds - {sortedNumbers}")
	return sortedNumbers


# The goal of this script is to calculate the time complexity of different sorting algorithms.

# Create an integer array to sort
if len(sys.argv) > 1:
	# Use integers given in command line
	numbers = []
	for arg in sys.argv[1:]:
		numbers.append(int(arg))
else:
	# No arguments given. Create an array of random size (1-100) with random integers in the range of -1000 to 1000
	numbers = []
	for i in range(random.randint(0, 100)):
		numbers.append(random.randint(-1000, 1000))


print(f"=====================================================================\nsorting the following {len(numbers)} integers: {numbers}\n")

print("Bubble sort:")
calculateTimeComplexity(bubbleSort, numbers.copy())

print("Faster bubble sort:")
calculateTimeComplexity(fasterBubbleSort, numbers.copy())

print("Selection sort:")
calculateTimeComplexity(selectionSort, numbers.copy())

print("Insertion sort:")
calculateTimeComplexity(insertionSort, numbers.copy())

print("Quick sort:")
calculateTimeComplexity(insertionSort, numbers.copy())

print("---------------------------------------------------------------------")






















