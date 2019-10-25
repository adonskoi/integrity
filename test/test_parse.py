import unittest

from integrity.parse import parse


content = [
    "file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906",
    "file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e",
    "file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e",
    "файл_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709",
]


class ParseFileTest(unittest.TestCase):
    def test_parse(self):
        files = parse(content, "/home/user")
        self.assertEqual(files[1].path, "/home/user/file_02.bin")
        self.assertEqual(files[3].name, "файл_04.txt")
        self.assertEqual(len(files), 4)
        self.assertEqual(files[3].alg, "sha1")
