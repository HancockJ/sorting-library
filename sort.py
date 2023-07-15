# Imports
import sys
import time
import random


def bubbleSort(numbers):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(numbers) - 1):
			if numbers[i] > numbers[i+1]:
				swapped = True
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
	return numbers


def fasterBubbleSort(numbers):
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
	sortedNumbers = [numbers.pop()]
	while(len(numbers) > 0):
		nextNumber = numbers.pop()
		broke = False
		for i in range(len(sortedNumbers)):
			if nextNumber < sortedNumbers[i]:
				sortedNumbers.insert(i, nextNumber)
				broke = True
				break
		if not broke:
			sortedNumbers.append(nextNumber)
	return sortedNumbers


def calculateTimeComplexity(func, numbers):
	start = time.time()
	sortedNumbers = func(numbers)
	end = time.time()
	print(f"Finished in {(end - start) * 1000000} microseconds - {sortedNumbers}")
	return sortedNumbers


# The goal of this script is to calculate the time complexity of different sorting algorithms.


if sys.argv.count == 1:
	# No arguments given
	# Create a random sized array (0-100) of random integers in the range of -1000 to 1000
	print('hi')
else:
	# Use integers given in command line
	numbers = []
	for arg in sys.argv[1:]:
		numbers.append(int(arg))

print(f"=====================================================================\nsorting the following {len(numbers)} integers: {numbers}\n")

print("Bubble sort:")
calculateTimeComplexity(bubbleSort, numbers.copy())

print("Faster bubble sort:")
calculateTimeComplexity(fasterBubbleSort, numbers.copy())

print("Selection sort:")
calculateTimeComplexity(selectionSort, numbers.copy())

print("Insertion sort:")
calculateTimeComplexity(insertionSort, numbers.copy())

print("---------------------------------------------------------------------")






















