# creates a mapping between a viewporton the complex plain and a window of pixels

class Mapper:
	def __init__(self, ll, ur, width, height):
		self.llOriginal = ll
		self.urOriginal = ur
		self.width = width
		self.height = height
		self.FitViewPort()

	def FitViewPort(self):
		horizontalScale = (self.urOriginal.real-self.llOriginal.real)/self.width
		verticalScale = (self.urOriginal.imag-self.llOriginal.imag)/self.height
		self.ll = self.llOriginal
		self.ur = self.urOriginal

	def Map(self, x, y):
		realPart = self.ll.real + x*(self.ur.real-self.ll.real)/self.width
		imagPart = self.ll.imag + y*(self.ur.imag-self.ll.imag)/self.height
		return complex(realPart, imagPart)


