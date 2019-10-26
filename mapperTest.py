from mapper import Mapper

def Test(mapper, x, y):
	result = mapper.Map(x, y)
	print('({0}, {1}) maps to {2} + {3}i'.format(x, y, result.real, result.imag))

ll = complex(-2, -2)
ur = complex(2, 2)

width = 100
height = 200
steps = 4

map = Mapper(ll, ur, width, height)

tests = range(steps+1)

for test in tests:
	Test(map, width*test/steps, height*test/steps)
