class Robot:
    """
       This is the fourth class
    """
    count = 0
    def __init__(self, name = None):
        self.name = name
        type(self).count += 1
    def __del__(self):
        type(self).count -= 1
    def say_hi(self):
        print(self.name, ', says "hi!"')
