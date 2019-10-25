import unittest
import hashlib
import sys, os

from integrity.calculate import is_hash_match

sha1_filetxt = "600f4f1a64be73f5bcc377caf50f6582f81d06c0"
sha256_filetxt = "2c873a1d80b479ace5e48a347254298a2b224a122849280f2bc88821a434462d"


class BasicHasherTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.alg = "md5"
        cmd = cls.alg + " -r "
        cls.filename = "integrity/__main__.py"
        if sys.platform == "darwin":
            process = os.popen(cmd + cls.filename)
        if sys.platform.startswith("linux"):
            process = os.popen(cls.alg + "sum " + cls.filename)
        cls.hash = process.read().split()[0]
        process.close()

    def test_ok(self):
        result = is_hash_match(self.filename, self.alg, self.hash)
        self.assertTrue(result == "OK")

    def test_file_not_found(self):
        result = is_hash_match("fil2e2.txt", self.alg, self.hash)
        self.assertTrue(result == "NOT FOUND")

    def test_sha1_not_raises(self):
        result = is_hash_match(self.filename, "sha1", self.hash)
        self.assertEqual(result, "FAIL")

    def test_sha256_not_raises(self):
        result = is_hash_match(self.filename, "sha256", self.hash)
        self.assertEqual(result, "FAIL")

    def test_wrong_hash_given_fail(self):
        wrong_hash = "a" * len(self.hash)
        result = is_hash_match(self.filename, self.alg, wrong_hash)
        self.assertTrue(result == "FAIL")

    def test_exception_with_wrong_algorithm(self):
        result = is_hash_match(self.filename, "jjj", "oweif")
        self.assertEqual(result, "WRONG ALG")

    def test_sha256(self):
        result = is_hash_match("test/file.txt", "sha256", sha256_filetxt)
        self.assertNotEqual(result, "WRONG ALG")

    def test_sha1(self):
        result = is_hash_match("test/file.txt", "sha1", sha1_filetxt)
        self.assertNotEqual(result, "WRONG ALG")

