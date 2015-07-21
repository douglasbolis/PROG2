def fazInsercao(lst):
	for j in range(len(lst)):
		x = lst[j]
		i = j-1

		while i >= 0 and lst[i] > x:
			lst[i+1] = lst[i]
			i = i-1
		# fim while
		lst[i+1] = x
	# fim for

	return lst
# fim fazInsercao

def main():
	print(fazInsercao([67, 34, 12, 200, 54, 2, 5, 13, 100]))
# fim main

main()
