# a = 5
# assert a == 3,"a should be {} but actually {}".format("3",a)

# assert 1+1 == 3 ,"1+2 not equal 2"

import unittest
class TestStingMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        #check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()