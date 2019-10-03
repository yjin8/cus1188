def merge_sort(arr):
	if  len(arr) > 1:
		l_index=0
		r_index= len(arr)-1
		split1 = int(l_index + ((r_index - l_index) / 3) + 1)
		split2 = int(l_index + 2 * ((r_index - l_index) / 3) + 1)
		left = arr[l_index:split1]
		mid = arr[split1:split2]
		right=arr[split2:r_index+1]

		merge_sort(left)
		merge_sort(mid)
		merge_sort(right)

		h = i = j = k = 0

		while h < len(left) and i < len(mid) and j < len(right):
			if left[h] < mid[i]:
				if left[h] < right[j]:
					arr[k] = left[h]
					h+=1
				else:
					arr[k] = right[j]
					j+=1
			else:
				if mid[i] < right[j]:
					arr[k] = mid[i]
					i+=1
				else:
					arr[k] = right[j]
					j+=1
			k+=1

		while h < len(left) and i < len(mid):
			if left[h] < mid[i]:
				arr[k] = left[h]
				h+=1
			else:
				arr[k] = mid[i]
				i+=1
			k+=1
			# print(arr)
		while i < len(mid) and j < len(right):
			if mid[i] < right[j]:
				arr[k] = mid[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
		while h < len(left) and j < len(right):
			if left[h] < right[j]:
				arr[k] = left[h]
				h+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
		while h < len(left):
			arr[k] = left[h]
			h+=1
			k+=1
		while i < len(mid): 
			arr[k] = mid[i]
			i+=1
			k+=1
		while j < len(right):
			arr[k] = right[j]
			j+=1
			k+=1
		return arr


if __name__ == '__main__':
	arr1 = [112,123,1,123,12,235,123,0]
	print("Input: " + str(arr1))
	print("Output: " + str(merge_sort(arr1)))
	arr2 = [12,457,234,12,34,1,2,3,346,123,23,434,142,1]
	print("Input: " + str(arr2))
	print("Output: " + str(merge_sort(arr2)))
