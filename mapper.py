# creates a mapping between a viewporton the complex plain and a window of pixels

class ViewPortMapper:
	def __init__(self, ll, ur, width, height):
		self.llOriginal = ll
		self.urOriginal = ur
		self.width = width
		self.height = height
		self.FitViewPort()

	def FitViewPort(self):
		horizontalScale = (self.urOriginal.real-self.llOriginal.real)/self.width
		verticalScale = (self.urOriginal.imag-self.llOriginal.imag)/self.height
		viewPortMidPoint = (self.llOriginal+self.urOriginal)/2
		if horizontalScale > verticalScale:
			self.ll = complex(self.llOriginal.real, 
										 viewPortMidPoint.imag+(self.llOriginal.imag-viewPortMidPoint.imag)*horizontalScale/verticalScale)
			self.ur = complex(self.urOriginal.real, 
										 viewPortMidPoint.imag+(self.urOriginal.imag-viewPortMidPoint.imag)*horizontalScale/verticalScale)
		else:
			self.ll = complex(viewPortMidPoint.real+(self.llOriginal.real-viewPortMidPoint.real)*verticalScale/horizontalScale, 
										 self.llOriginal.imag)
			self.ur = complex(viewPortMidPoint.real+(self.urOriginal.real-viewPortMidPoint.real)*verticalScale/horizontalScale, 
										 self.urOriginal.imag)

	def Map(self, x, y):
		realPart = self.ll.real + x*(self.ur.real-self.ll.real)/self.width
		imagPart = self.ll.imag + y*(self.ur.imag-self.ll.imag)/self.height
		return complex(realPart, imagPart)


