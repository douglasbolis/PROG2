def insercaoSort(param_lst):
	lst_result = []
	
	if len(param_lst) > 0:
		lst_result.append(param_lst[0])
		lst_corrente = param_lst[1:]
	else:
		return []
	# fim else:
	
	for i in range(len(lst_corrente)):
		for j in range(len(lst_result)):
			if lst_corrente[i] > lst_result[j]:
				lst_result.insert(j+1, lst_corrente[i])
			else:
				if i == 0:
					lst_result.insert(0, lst_corrente[i])
				else:
					lst_result.insert(j-1, lst_corrente[i])
				# fim else
			# fim else
		# fim for
	# fim for
	
	return lst_result
# fim insercaoSort

def main():
	print(insercaoSort([67, 34, 12, 34, 54, 2, 5, 13]))
# fim main

main()
