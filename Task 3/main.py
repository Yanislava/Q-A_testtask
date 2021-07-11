import time
import psutil
import os
import pathlib
from abc import ABC, abstractmethod


class TestPrototype(ABC):

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    @abstractmethod
    def prep(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def clean_up(self):
        print("clean_up() successfully finished")
        pass

    def execute(self):
        print(f"Test id is {self.tc_id}\nTest name is {self.name}\n")
        self.prep()
        if type(self) == FileList:

            try:
                self.run()
            except FileNotFoundError:
                print("File or directory not found")

        elif type(self) == RandomFile:

            if not os.path.exists("test.txt"):
                self.run()
            else:
                write = True
                while write:
                    overwrite = input("File test.txt already exists. Do you want to overwrite it?\nType 'y' or 'n'\n")
                    if overwrite.lower() == "y":
                        write = False
                        self.run()
                    elif overwrite.lower() == "n":
                        write = False
                        print("run() has been canceled by user")
                    else:
                        print("Invalid input. Please, enter 'y' or 'n'\n")
        try:
            self.clean_up()
            print(f"Test {self.tc_id} named {self.name} has been successfully finished\n")
        except FileNotFoundError:
            print(f"File test.txt not found.\nTest {self.tc_id} named {self.name} has been finished.\n"
                  "clean_up() has not been completed")


class FileList(TestPrototype):

    def prep(self):
        cur_time = round(time.time())
        if cur_time % 2 != 0:
            print("prep() has been successfully finished. Current system time in seconds is a multiple of 2")
            return
        else:
            print("prep() has been successfully finished. Current system time in seconds is not a multiple of 2")

    def run(self):
        dir_list = os.listdir(pathlib.Path.home())
        for i in dir_list:
            print(i)
        print("run() has been successfully finished")


class RandomFile(TestPrototype):

    def prep(self):
        memory_gb = psutil.virtual_memory().total/(1000**3)
        if memory_gb < 1:
            print("prep() successfully finished. RAM of current computer is less than 1 Gb")
            return
        else:
            print("prep() successfully finished. RAM of current computer is more than 1 Gb")

    def run(self):
        with open("test.txt", "wb") as file:
            file.write(os.urandom(1024000))
            print(f"run() successfully finished. File test.txt has been created.\n"
                  f"The size is {os.path.getsize('test.txt')/1000} Kilobytes")

    def clean_up(self):
        os.remove("test.txt")
        print("clean_up() successfully finished. File test.txt has been deleted")
        

a = FileList(1, "First")
b = RandomFile(2, "Second")

a.execute()
b.execute()



