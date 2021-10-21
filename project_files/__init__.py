

from project_files.src.DatabaseModules import DatabaseSettings
import sys


class MainController(object):
    def __init__(self):
        pass

    def run(self):
        print("sys.argv", sys.argv)
        print("run")
        d = DatabaseSettings()
        print(d)

