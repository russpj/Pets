from mapper import ViewPortMapper

def Test(mapper, x, y):
	result = mapper.Map(x, y)
	print('({0}, {1}) maps to {2}'.format(x, y, result))

def RunTests(mapper, steps):
	print('run of {0} steps covering {1} to {2}'.format(steps+1, mapper.llOriginal, mapper.urOriginal))
	print('expanded range is {0} to {1}'.format(mapper.ll, mapper.ur))
	tests = range(steps+1)
	for test in tests:
		Test(map, width*test/steps, height*test/steps)

ll = complex(-1, -1)
ur = complex(3, 3)

width = 100
height = 200
steps = 4

map = ViewPortMapper(ll, ur, width, height)

RunTests(map, steps)
