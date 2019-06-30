#Interview Question
# Find pairs of numbers in a list which sums up to expected sum in linear time

def arrSum(arrayList, exp_sum):
	temp_dict = {}
	return_dict = {}
	for num in arrayList:
		if num:
			temp_dict[num] = exp_sum-num
	print(temp_dict)

	for key,val in temp_dict.items():
		if val in arrayList:
			if key in return_dict.keys() or val in return_dict.keys():
				pass
			else:
				return_dict[key]=val
	return return_dict






