from Split_string import solution
import unittest

class Test_solution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('dfqt'),['df','qt'])
        


if __name__=='__main__':
        unittest.main()