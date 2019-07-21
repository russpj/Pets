import rotate
import animator

test = []

for n in range(10):
	test.append(n)

def AnimStep():
	print(test)
	
def TestOnce(description, list, size, rotator, offset):
	print('{0} {1}'.format(description, offset))
	print(list)
	rotator(list, 0, size, offset)
	print(list)
	print('{0} {1}'.format(description, size-offset))
	rotator(list, 0, size, size-offset)
	print(list)

TestOnce('By Reverse', test, 10, rotate.RotateRev, 4)

TestOnce('By Round Robin', test, 10, rotate.RotateRound, 4)

TestOnce('By Swap', test, 10, rotate.RotateSwap, 4)


