from time import sleep, time
import numpy
import os

class Logger():
    def __init__(self, filename, path = os.getcwd()):
        self.filename = filename
        self.path = path
        
    def append(self, *argv, **kwargs):
        self.append_end_NL(argv)    
    
    def append_end_NL(self, *argv, **kwargs):
        access_method = 'a'
        log = open(self.path + '/' + self.filename, access_method)
        line = []
        for arg in argv:
            if type(arg) == list or type(arg) == numpy.array or type(arg) == numpy.ndarray:
                for entry in arg:
                    line.append(entry)
            else: line.append(arg)
        log.write(", ".join([str(sth) for sth in line]))
        log.write("\r\n")
        log.close
        
    def append_start_NL(self, *argv, **kwargs):
        access_method = 'a'
        log = open(self.path + '/' + self.filename, access_method)
        log.write("\r\n")
        line = []
        for arg in argv:
            if type(arg) == list or type(arg) == numpy.array or type(arg) == numpy.ndarray:
                for entry in arg:
                    line.append(entry)
            else: line.append(arg)
        log.write(", ".join([str(sth) for sth in line]))
        log.close
        
    def append_inline(self, *argv, access_method = 'a', **kwargs):
        log = open(self.path + '/' + self.filename, access_method)
        line = []
        for arg in argv:
            if type(arg) == list or type(arg) == numpy.array or type(arg) == numpy.ndarray:
                for entry in arg:
                    line.append(entry)
            else: line.append(arg)
        log.write(", ".join([str(sth) for sth in line]))
        log.close
        
    def erase(self, permission = 'n',):
        if permission != 'y':
            permission = input("Type 'y' to permit file erase {}\n".format(self.filename))
        if permission == 'y':
            open(self.path + '/' + self.filename, "w").close()
        else: 
            print("User skipped file erase")


if __name__ == "__main__":
    log = Logger(filename = 'log.csv')
    print(log.filename)
    print(log.path)
    log.erase()
    log.append_end_NL([1,2,3,5],"test", "ciastka", filename = 'log.csv', access_method = 'a')