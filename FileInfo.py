import os
from sys import argv


class Files():
    theFile=""

   #initilize incomeing file#
    def __init__(self,file):
        self.theFile = file
     #returns the tail of the path#
    def fileName(self):
        self.tail = os.path.basename(self.theFile)
        return "file name: "+self.tail

    #get file size#
    def fileSize(self):
        self.size = os.path.getsize(self.theFile)
        return str(self.size)

   #checking if its a file
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
#remove commnet for cmd line usage#
#main(*argv[1:])
