import unittest 
from df_utils import TEST_DF, Processor


class ProcessorTests(unittest.TestCase):
    """Test Functions in Processor class!"""
    def test_missingvalues(self):
        proc = Processor()
        df = TEST_DF
        self.assertEqual(proc.missing_values(df), None)


if __name__ == '__main__':
    unittest.main()