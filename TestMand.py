class Mapper:
	def __init__(self, ll, ur, width, height):
		self.llOriginal = ll
		self.urOriginal = ur
		self.width = width
		self.height = height

	def FitViewPort(self):
		horizontalScale = (ur.real-ll.real)/width
		verticalScale = (ur.imag-ll.imag)/height

	def Map(self, x, y):
		realPart = ll.real + x*(ur.real-ll.real)/width
		imagPart = ll.imag + y*(ur.imag-ll.imag)/height
		return complex(realPart, imagPart)

def Test(mapper, x, y):
	result = mapper.Map(x, y)
	print('({0}, {1}) maps to {2} + {3}i'.format(x, y, result.real, result.imag))

ll = complex(-2, -2)
ur = complex(2, 2)

width = 100
height = 200
steps = 4

mapper = Mapper(ll, ur, width, height)

tests = range(steps+1)

for test in tests:
	Test(mapper, width*test/steps, height*test/steps)
