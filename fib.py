def FibRec(n):
	if n < 2: return 1
	return FibRec(n-1)+FibRec(n-2)
	
print(FibRec(5))

def FibIter(n):
	first=1
	second=1
	n-=2
	while(n>=0):
		third=first+second
		first=second
		second=third
		n=n-1
	return second

print(FibIter(5))

import time;

def TimeFun(fun, n):
	start = time.time()
	value = fun(n)
	end = time.time()
	return (value, end-start)

def TimeFibs(n):
	rec = TimeFun(FibRec, n)
	iter = TimeFun(FibIter, n)
	return [rec, iter]

for n in range(35):
	print(TimeFibs(n))