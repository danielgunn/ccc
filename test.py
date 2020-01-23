import unittest
from unittest.mock import patch
import io
from io import StringIO

class TestAllYears(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_2019_j1(self, mock_stdout):
        from y2019 import j1
        import glob, os

        # for each input test
        for filename in glob.iglob('y2019/all_data/j1/**.in', recursive=True):
            if os.path.isfile(filename):
                with open(filename, 'r') as inf:
                    input_data = inf.read()
                    with open(filename[:-3] + ".out", 'r') as outf:
                        output_data = outf.read()

                        # patch the input and assert the output
                        with patch('sys.stdin', StringIO(input_data)):
                            j1.main()
                            res = mock_stdout.getvalue()
                            self.assertEqual(output_data, res, msg='failed {0} with output {1}'.format(filename[:-3], bytes(res, "utf-8").decode("unicode_escape")))
                        mock_stdout.seek(0)
            assert True


if __name__ == '__main__':
    unittest.main()
