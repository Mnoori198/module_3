import unittest
import unittest.mock as mock
from main_page import average_score


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=([90, 85, 95])):
            assert average_score.average() == 90
    # assert average_score.average() == 90



if __name__ == '__main__':
    unittest.main()
