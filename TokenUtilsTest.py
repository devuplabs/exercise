import unittest
from TokenUtils import TokenUtils


class TokenUtilsTest(unittest.TestCase):
    def test_get_tokens(self):
        tokenizer = TokenUtils()
        expected_tokens = ["This", "is", "a", "test"]
        actual_tokens = tokenizer.get_tokens("This is a test")
        self.assertEqual(expected_tokens, actual_tokens)

    def test_get_top2tokens(self):
        tokenizer = TokenUtils()
        expected_tokens = ["blue", "red"]
        actual_tokens = tokenizer.get_topn_tokens("red, blue, red, green, blue, blue, red, red, red", 2)
        self.assertEqual(expected_tokens, actual_tokens)


if __name__ == '__main__':
    unittest.main()
