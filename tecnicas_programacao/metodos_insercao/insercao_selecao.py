def insercaoSort(param_lst):
	lst_result, trocas = [], 0
	
	if len(param_lst) > 0:
		lst_result.append(param_lst[0])
		lst_corrente = param_lst[1:]
		trocas += 1
	else:
		return []
	# fim else
	
	for i in range(len(lst_corrente)):
		m, inseriu = 0, False

		while m < (len(lst_result)) and not inseriu:
			if lst_corrente[i] < lst_result[m]:
				lst_result.insert(m, lst_corrente[i])
				trocas += 1
				inseriu = True
			elif lst_corrente[i] > lst_result[len(lst_result)-1]:
				lst_result.insert(len(lst_result), lst_corrente[i])
				trocas += 1
				inseriu = True
			elif lst_corrente[i] > lst_result[m] and lst_corrente[i] < lst_result[m+1]:
				lst_result.insert(m+1, lst_corrente[i])
				trocas += 1
				inseriu = True
			# fim elif

			m += 1
		# fim while
	# fim for

	print(trocas)
	return lst_result
# fim insercaoSort

def main():
	print(insercaoSort([67, 34, 12, 200, 54, 2, 5, 13, 100]))
# fim main

main()
