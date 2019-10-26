from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
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
		grid = GridLayout(cols=2)

		ll = complex(-2.0, -2.0)
		ur = complex(2.0, 2.0)
		caption = 'Mandelbrot Set on grid from {0} to {1}'.format(ll, ur)

		hello = Button(text='Hello World')
		hello.background_color = [1, 0, 1, 1]
		grid.add_widget(hello)

		grid.add_widget(Arena())

		return grid

if __name__ == '__main__':
	MandApp().run()
