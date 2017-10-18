import hashlib
import os


def fileMD(self):
        salt_ = os.urandom(32).hex()
        hash_object = hashlib.md5()
        hash_object.update(('%s%s' % (salt_, self.theFile)).encode('utf-8'))
        print("MD5 Hash: "+hash_object.hexdigest())