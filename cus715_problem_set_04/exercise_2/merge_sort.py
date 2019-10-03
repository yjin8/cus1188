def merge_sort(arr):
	if  len(arr) > 1:
		l_index=0
		r_index= len(arr)-1
		split1 = int(l_index + ((r_index - l_index) / 3) + 1)
		split2 = int(l_index + 2 * ((r_index - l_index) / 3) + 1)
		left = arr[l_index:split1]
		mid = arr[split1:split2]
		right=arr[split2:r_index+1]
		# print(left, end= ' ')
		# print(mid , end= ' ')
		# print(right)

		merge_sort(left)
		merge_sort(mid)
		merge_sort(right)

		h = i = j = k = 0
		# if len(left)== 0 and len(right)==0:
		# 	h = -1
		# if len(mid) == 0:
		# 	i = -1
		# if len(right) == 0:
		# 	j == -1
		while h < len(left) and i < len(mid) and j < len(right):
			if left[h] < mid[i] and left[h] < right[j]:
				arr[k] = left[h]
				h+=1
			elif mid[i] < left[h] and mid[i] < right[j]:
				arr[k] = mid[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
			print(arr)
		while h < len(left) and i < len(mid):
			if left[h] < mid[i]:
				arr[k] = left[h]
				h+=1
			else:
				arr[k] = mid[i]
				i+=1
			k+=1
			print(arr)
		while h < len(left) and j < len(right):
			if left[h] < right[j]:
				arr[k] = left[h]
				h+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
			print(arr)
		while i < len(mid) and j < len(right):
			if mid[i] < right[j]:
				arr[k] = mid[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
			print(arr)
		while h < len(left):
			arr[k] = left[h]
			h+=1
			k+=1
			print(arr)
		while i < len(mid): 
			arr[k] = mid[i]
			i+=1
			k+=1
			print(arr)
		while j < len(right):
			arr[k] = right[j]
			j+=1
			k+=1
			print(arr)
		return arr

def merge(left,mid,right,arr):
	h = i = j = k = 0
	if not left or not mid or not right:
		print('yo')
	while h < len(left) and i < len(mid) and j < len(right):
		if left[h] < mid[i] and left[h] < right[j]:
			arr[k] = left[h]
			h+=1
		elif mid[i] < left[h] and mid[i] < right[j]:
			arr[k] = mid[i]
			i+=1
		else:
			arr[k] = right[j]
			j+=1
		k+=1
	return arr

#print(merge([4], [], [23],[0,0,0]))

print(merge_sort([1,2,3,4,23,21,2,52,23,4,12,1,32,123]))
# merge_sort([1,2,3],0,2)

def recurs(arr):
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements  
		print(L, end=' ')
		R = arr[mid:] # into 2 halves 
		print(R)
  
		recurs(L) # Sorting the first half 
		recurs(R) # Sorting the second half 

# recurs([1,2,3,4,5,6,7,8,9,10,11,12])

def split(arr):
	if  len(arr) > 1:
		l_index=0
		r_index= len(arr)-1
		split1 = int(l_index + ((r_index - l_index) / 3) + 1)
		# print(split1)
		split2 = int(l_index + 2 * ((r_index - l_index) / 3) + 1)
		# print(split2)
		left = arr[l_index:split1]
		mid = arr[split1:split2]
		right=arr[split2:r_index+1]
		print(left, end= ' ')
		print(mid , end= ' ')
		print(right)

		split(left)
		split(mid)
		split(right)
		print(left)
		print(right)
		print()

split([12,1])