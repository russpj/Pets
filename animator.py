

class Animator:
    def Execute(self):
        if callback is not None:
            callback()

    def SetCallback(newCallback):
        self.callback = newCallback

    def PrintIfNoCallback(self, message):
        if self.callback is None:
            print(message)

    callback = None
