from reverse import Reverse
from reverse import Swap

def AnimStepperDefault():
	return
	
AnimStepper = AnimStepperDefault

def SetupAnim(animStep):
	global AnimStepper
	AnimStepper = animStep

def RotateRev(list, begin, end, offset):
	Reverse(list, begin, offset)
	AnimStepper()
	Reverse(list, offset, end)
	AnimStepper()
	Reverse(list, begin, end)
	AnimStepper()
	return
	
def GetNext(current, offset, begin, end):
	next = current + offset
	if next >= end:
		next = begin+next-end
	return next
	
def RotateRound(list, begin, end, offset):
	start = begin
	moved = 0
	while moved < end-begin:
		first = start
		second = GetNext(first, offset, begin, end)
		while second != start:
			Swap(list, first, second)
			AnimStepper()
			moved = moved+1
			first = second
			second = GetNext(second, offset, begin, end)
		start = start+1
		moved = moved+1
	return
		
def SwapRange(list, begin, end, other):
	while begin<end:
		Swap(list, begin, other)
		begin=begin+1
		other=other+1
	AnimStepper()
	return
	
def RotateSwap(list, begin, end, offset):
	if offset==0:
		return
	if begin==end:
		return
	if offset==end-begin:
		return
	if offset <= (end-begin)/2:
		SwapRange(list, begin, begin+offset, begin+offset)
		RotateSwap(list, begin+offset, end, offset)
	else:
		rangeSize = (end-begin)-offset
		SwapRange(list, begin, begin+rangeSize, begin+offset)
		RotateSwap(list, begin+rangeSize, end, offset-rangeSize)
	return