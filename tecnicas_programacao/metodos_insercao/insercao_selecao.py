__author__ = 'douglas'

def selectionSort(param_lst):
	lst_result, trocas = [], 0

	for i in range(len(param_lst)-1):
		minimo = i
		j = i+1

		while j < len(param_lst):
			if param_lst[j] < param_lst[minimo]:
				minimo = j
			# fim if

			j += 1
		# fim for

		if (param_lst[i] != param_lst[minimo]):
			trocas += 1
		# fim if

		param_lst[i], param_lst[minimo] = param_lst[minimo], param_lst[i]
	# fim for

	return lst_result, trocas
# fim selectionSort