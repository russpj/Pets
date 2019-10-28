from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from mapper import ViewPortMapper

class Arena(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ll = complex(-2, -2)
		self.ur = complex(2, 2)
		self.UpdateCanvas()

	def SetComplexRange(self, ll, ur):
		self.ur = ur
		self.ll = ll
		self.UpdateWindowSize()

	def UpdateWindowSize(self):
		self.mapper = ViewPortMapper(self.ll, self.ur, self.width, self.height)

	def UpdateCanvas(self):
		self.canvas.clear()
		with self.canvas:
			Color(0.7, 0.7, 0.1)
			Ellipse(pos=self.pos, size=self.size)

def ColorMapper(z):
	dist = abs(z)*100
	if dist > 255:
		dist = 255
	return int(dist)

def MixColors(color1, color2, ratio):
	red = color1.r*(1-ratio) + color2.r*ratio
	green = color1.g*(1-ratio) + color2.g*ratio
	blue = color1.b*(1-ratio) + color2.b*ratio
	return Color(red, green, blue)

class MandApp(App):
	def build(self):
		self.root = layout = FloatLayout()
		layout.bind(size=self._update_rect, pos=self._update_rect)

		self.ll = complex(-2.0, -2.0)
		self.ur = complex(2.0, 2.0)
		self.caption = 'Mandelbrot Set on grid from {0} to {1}'.format(self.ll, self.ur)

		with layout.canvas.before:
			Color(0.1, .9, 0.1, 1)  # green; colors range from 0-1 not 0-255
			self.rect = Rectangle(size=layout.size, pos=layout.pos)
			Color(0.1, .1, .9, 1)
			self.ellipse = Ellipse(size=layout.size, pos=layout.pos)

		return layout

	def _update_rect(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size
		instanceX = instance.pos[0]
		instanceY = instance.pos[1]
		instanceWidth = instance.size[0]
		instanceHeight = instance.size[1]
		if instanceWidth < instanceHeight:
			ellipseSize = [instanceWidth, instanceWidth]
			ellipsePos = [instanceX, instanceY - (instanceWidth-instanceHeight)/2]
		else:
			ellipseSize = [instanceHeight, instanceHeight]
			ellipsePos = [instanceX - (instanceHeight-instanceWidth)/2, instanceY]
		self.ellipse.pos = ellipsePos
		self.ellipse.size = ellipseSize
		Clock.schedule_once(self.CalculateMandelbrotDisplay, 1)

	def CalculateMandelbrotDisplay(self, dt):
		colorMin = Color(1, 0, 0)
		colorMax = Color(0, 1, 0)
		windowWidth = int(self.rect.size[0])
		windowHeight = int(self.rect.size[1])
		mapper = ViewPortMapper(self.ll, self.ur, windowWidth, windowHeight)
		self.display = []
		for x in range(windowWidth):
			self.display.append([])
			for y in range(windowHeight):
				z = mapper.Map(x, y)
				self.display[x].append(MixColors(colorMin, colorMax, ColorMapper(z)/256))
		self.PaintMandelbrot()
	
	def PaintMandelbrot(self):
		canvas = self.root.canvas
		canvas.clear()
		with canvas:
			for x in range(self.root.size[0]):
				Color(0,0,0)
				Rectangle(pos=[x,0], size=[1, self.root.size[1]])
				for y in range(self.root.size[1]):
					Color(self.display[x][y])
					Rectangle(pos=[x,y], size=[1,1])

if __name__ == '__main__':
	MandApp().run()
