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
	return quickSort(left) + [pivot] + quickSort(right)


def mergeSort(numbers):
	# Base case
	if len(numbers) <= 1:
		return numbers
	else:
		# Split array into 2 equal sized arrays (+1 on left if odd # of elements)
		split = len(numbers) // 2
		left = mergeSort(numbers[:split])
		right = mergeSort(numbers[split:])
		l, r = 0, 0
		merged = []

		# Merge the 2 sorted arrays together
		while l < len(left) and r < len(right):
			if left[l] < right[r]:
				merged.append(left[l])
				l += 1
			else:
				merged.append(right[r])
				r += 1

		# Append the remaining sorted elements
		if l < len(left):
			merged += left[l:]
		if r < len(right):
			merged += right[r:]
		return merged

# Sub routine version of counting sort, sorts by digit place (1, 10, 100, etc)
def countingSort(numbers, digitPlace):
	# Calculate count for each digit
	count = [0] * 10
	for i in numbers:
		count[(abs(i) // digitPlace) % 10] += 1

	# Convert count to the cumulative sum for each digit
	for i in range(1,10):
		count[i] += count[i - 1]

	# Create an array the size of original array
	sortedArray = [0] * len(numbers)

	# Fill new array with old array values based on count array index
	for i in numbers[::-1]:
		sortedArray[count[(abs(i) // digitPlace) % 10] - 1] = i
		count[(abs(i) // digitPlace) % 10] -= 1

	return sortedArray


def radixSort(numbers):
	maximum = max(numbers) if max(numbers) > abs(min(numbers)) else abs(min(numbers))

	digitPlace = 1
	while maximum // digitPlace > 0:
		numbers = countingSort(numbers, digitPlace)
		digitPlace *= 10

	# Seperate negative numbers and reverse them
	negative, positive = [], []
	for i in numbers:
		if i < 0:
			negative.append(i)
		else:
			positive.append(i)

	# Return concattenated list of sorted numbers
	return negative[::-1] + positive



def calculateTimeComplexity(func, numbers):
	start = time.time()
	sortedNumbers = func(numbers)
	end = time.time()
	print(f"Finished in {(end - start) * 1000000} microseconds.")
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

# For testing
#numbers = [848, 287, 225, 932, -469, -390, -91, 413, 500, 575, 26, -371, 477, 148, -881, 244, 648, -491, 58, -76, 340, 73, -481, 29, 72, -249, -783, 107, -938, -640, -937, 938, -988, 163, -181, 127, 455, 289, -557, 172, 575, 178, -292, 347, -622, 321, 578, -392, -722, 490, -475, -667, 55, -279, -446, -978, 923, -495, 899, 67, 677, -472, -470, -780, 103, -151, 227, -893, 263, 848, -335, -861, -704, -852, 283, -792, 345, 662, -930, -218, 120, -97, -646, 330, -341, 122, 61, -879, -411, 910, 537, 331, -735, 933, -617]


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
calculateTimeComplexity(quickSort, numbers.copy())

print("Merge sort:")
calculateTimeComplexity(mergeSort, numbers.copy())

print("Radix sort:")
calculateTimeComplexity(radixSort, numbers.copy())

print("---------------------------------------------------------------------")






















