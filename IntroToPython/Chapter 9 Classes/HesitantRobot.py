 1 from Robot_IX import Robot
 2 
 3 class HesitantRobot(Robot):
 4     def __init__(self, name = None, times = 1):
 5         super().__init__(name = name)
 6         self.__times = times
 7 
 8     def say_hi(self):
 9         print('"', 'um ...' * self.__times, 'hi!", said', super().name)
10 
11     def say_goodbye(self):
12         print('"', 'um ...' * self.__times, 'goodbye!", said', super().name)