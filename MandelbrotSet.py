from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
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


class MandApp(App):
	def build(self):
		self.root = layout = FloatLayout()
		layout.bind(size=self._update_rect, pos=self._update_rect)

		ll = complex(-2.0, -2.0)
		ur = complex(2.0, 2.0)
		caption = 'Mandelbrot Set on grid from {0} to {1}'.format(ll, ur)

		with layout.canvas.before:
			Color(0.1, .9, 0.1, 1)  # green; colors range from 0-1 not 0-255
			self.rect = Rectangle(size=layout.size, pos=layout.pos)
			Color(0.1, .1, .9, 1)
			self.ellipse = Ellipse(size=layout.size, pos=layout.pos)

		return layout

	def _update_rect(self, instance, value):
		self.ellipse.pos = self.rect.pos = instance.pos
		self.ellipse.size = self.rect.size = instance.size
		

if __name__ == '__main__':
	MandApp().run()
