def merge_sort(array):
	n = len(array)
	
	if n <= 1:
		return array

	middle = n // 2

	left = merge_sort(array[0 : middle])
	right = merge_sort(array[middle : n])

	return merge(left, right)

def merge(a, b):
	array = []
    
	while a and b:
		if a[0] > b[0]:
			array.append(b[0])
			del b[0]
        
		else:
			array.append(a[0])
			del a[0]
    
	while a:
		array.append(a[0])
		del a[0]
    		
	while b:
		array.append(b[0])
		del b[0]
    
	return array
