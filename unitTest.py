import unittest
from sha1Digest import fileSha
from md5Digest import fileMD
from FileInfo import Files

class TestFunctions(unittest.TestCase):
    def test_File_SHA(self):
        self.assertNotEqual(fileSha("testFile.txt"),fileSha("testFile.txt"),"Please Check Your Data")

    def test_File_MD5(self):
        self.assertNotEqual(fileMD("testFile.txt"), fileSha("testFile.txt"))

    def test_File_Size(self):
        fl = Files("testFile.txt")
        fs = Files("testFile.txt")
        self.assertTrue(fs,fl)

if __name__ == '__main__':
    unittest.main(exit=False)