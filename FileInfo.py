import os
from sys import argv


class Files():
    theFile=""


    def __init__(self,file):
        self.theFile = file

    def fileName(self):
        self.tail = os.path.basename(self.theFile)
        return "file name: "+self.tail


    def fileSize(self):
        self.size = os.path.getsize(self.theFile)
        return str(self.size)


    def isFile(self):
        if not os.path.isfile(self.theFile):
            return False
        else:
            return True


    #def fileSha(self):


    #def fileMD(self):





def main(fileString):
    fl = Files(fileString)
    if fl.isFile():
        print(fl.fileName())
        print(fl.fileSize())


    else:
        print("File Could Not Be Found.")

#main(*argv[1:])
