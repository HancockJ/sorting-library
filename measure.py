import time

def timeComplexity(func, numbers):
	start = time.time()
	sortedNumbers = func(numbers)
	end = time.time()
	print(f"Finished in {(end - start) * 1000000} microseconds.")
	return sortedNumbers
