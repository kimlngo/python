import unittest
import Cap

class CapTest(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = Cap.capitalize_text(text)

        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        text = 'python is simple'
        result = Cap.capitalize_text(text)

        self.assertEqual(result, 'Python Is Simple')

if __name__ == '__main__':
    unittest.main()