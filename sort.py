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
