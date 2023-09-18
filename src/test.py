from tex import Tex
import unittest

class TestFileCopy(unittest.TestCase):   
    def test_copying(self):
        tex = Tex.from_file("src/data/target.tex")
        tex._write("src/data/copy.tex")

        with open("src/data/copy.tex", "rb") as f:
            source = bytearray(f.read())
        with open("src/data/target.tex", "rb") as f:
            copy = bytearray(f.read())
        
        self.assertEqual(source, copy)

if __name__ == '__main__':
    unittest.main()