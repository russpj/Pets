

class Animator:
	def Execute(self):
		if self.callback is not None:
			self.callback()

	def SetCallback(newCallback):
		self.callback = newCallback

	def PrintIfNoCallback(self, message):
		if self.callback is None:
			print(message)

	callback = None
