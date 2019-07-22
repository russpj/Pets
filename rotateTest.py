import rotate
import animator

test = []

for n in range(10):
	test.append(n)

animator = animator.Animator()
	
def TestOnce(description, list, size, rotator, offset, animator):
	print('{0} {1}'.format(description, offset))
	print(list)
	rotator(list, 0, size, offset)
	animator.PrintIfNoCallback(list)
	print('{0} {1}'.format(description, size-offset))
	rotator(list, 0, size, size-offset)
	animator.PrintIfNoCallback(list)

TestOnce('Rotate by Reverse', test, 10, rotate.RotateRev, 4, animator)

TestOnce('Rotate by Round Robin', test, 10, rotate.RotateRound, 4, animator)

TestOnce('Rotate by Swap', test, 10, rotate.RotateSwap, 4, animator)


