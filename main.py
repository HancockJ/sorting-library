# External imports
import sys
import random

# My imports
import sort # sort.py (Contains different sorting algorithms)
import measure # measure.py (Contains different measurement tools for processes)

# Main script to test different sorting algorithms in python.

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

# For testing (If you want to keep a constant seed value)
#numbers = [848, 287, 225, 932, -469, -390, -91, 413, 500, 575, 26, -371, 477, 148, -881, 244, 648, -491, 58, -76, 340, 73, -481, 29, 72, -249, -783, 107, -938, -640, -937, 938, -988, 163, -181, 127, 455, 289, -557, 172, 575, 178, -292, 347, -622, 321, 578, -392, -722, 490, -475, -667, 55, -279, -446, -978, 923, -495, 899, 67, 677, -472, -470, -780, 103, -151, 227, -893, 263, 848, -335, -861, -704, -852, 283, -792, 345, 662, -930, -218, 120, -97, -646, 330, -341, 122, 61, -879, -411, 910, 537, 331, -735, 933, -617]


print(f"=====================================================================\nSorting the following {len(numbers)} integers: {numbers}\n")

print(f"Sorted array: {sort.bubbleSort(numbers.copy())}\n")

print("Bubble sort:")
measure.timeComplexity(sort.bubbleSort, numbers.copy(),)

print("Faster bubble sort:")
measure.timeComplexity(sort.fasterBubbleSort, numbers.copy())

print("Selection sort:")
measure.timeComplexity(sort.selectionSort, numbers.copy())

print("Insertion sort:")
measure.timeComplexity(sort.insertionSort, numbers.copy())

print("Quick sort:")
measure.timeComplexity(sort.quickSort, numbers.copy())

print("Merge sort:")
measure.timeComplexity(sort.mergeSort, numbers.copy())

print("Radix sort:")
measure.timeComplexity(sort.radixSort, numbers.copy())

print("---------------------------------------------------------------------")


# TODO:
# - Create a function to run each algorithm X amount of times with a different random set of numbers and then calculate average time taken.
# - Make it easy to choose all of your preferred inputs via command line arguments or other methods (range of integers, range of integer array size, times to run, etc...).
# - Integrate more measurements like space complexity.
# - Add in more sorting methods.























