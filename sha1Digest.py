import hashlib
import os


def fileSha(self):
        salt_ = os.urandom(32).hex()
        hash_object = hashlib.sha1()
        hash_object.update(('%s%s' %(salt_,self.theFile)).encode('utf-8'))
        print("SHA1 Hash: "+hash_object.hexdigest())