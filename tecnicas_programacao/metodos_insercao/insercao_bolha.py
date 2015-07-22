__author__ = 'douglas'

def bubbleSort(lst):
	trocas = 0

	for i in range(len(lst)):
		for j in range(len(lst)-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
				trocas += 1
			# fim if
		# fim for
	# fim for

	return lst, trocas
# fim bubbleSort