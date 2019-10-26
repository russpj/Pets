from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class Arena(Widget):
	def CalcDrawableRect(self):
		windowSize = self.size
		verticalFactor = self.height/(self.ur.imaginary - self.ll.imaginary)
		horizontalFactor = self.width/(self.ur.real - self.ll.real)
		if verticalFactor<horizontalFactor:
			horizontalFactor = verticalFactor
		else:
			verticalFactor = horizontalFactor



	def SetComplexRange(self, ll, ur):
		self.ur = ur
		self.ll = ll

class MandApp(App):
	def build(self):
		grid = GridLayout(cols=2)

		hello = Button(text='Hello World')
		hello.background_color = [1, 0, 1, 1]
		grid.add_widget(hello)

		grid.add_widget(Arena())

		return grid

if __name__ == '__main__':
	MandApp().run()
