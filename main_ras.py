import time
import sys

from daemons.prefab import step


class run_daemo(step.StepDaemon):

    def step(self):
        time.sleep(10)
        cs = Control_Sensor.getInstance()

    def __del__(self):
        print('it stop')


class Control_Sensor():
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        print('it is instan')
        if Control_Sensor.__instance == None:
            Control_Sensor()
        return Control_Sensor.__instance

    def __init__(self):
        if Control_Sensor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Control_Sensor.__instance = self

    def get_value(self):
        sys.stdout.write('it get value')

    def setPinToControl(self, pins, switch):
        sys.stdout.write(str(pins)+'\n')
        sys.stdout.write(str(switch)+'\n')

    def __del__(self):
        print('it del ')
