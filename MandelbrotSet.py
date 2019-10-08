import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Color

class MandApp(App):
	def build(self):
		text = Label(text="Hello World!")
		return text

if __name__ == '__main__':
	MandApp().run()
