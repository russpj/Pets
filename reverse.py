
def Swap(list, one, other):
	temp = list[one]
	list[one] = list[other]
	list[other] = temp

def Reverse(list, begin, end):
	while begin < end:
		Swap(list, begin, end-1)
		begin = begin+1
		end = end-1
