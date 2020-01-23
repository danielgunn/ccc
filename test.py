import unittest
from unittest.mock import patch
import io
from io import StringIO

class TestAllYears(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def check_question_data(self, module, data_folder, mock_stdout):
        import glob, os

        # for each input test
        for filename in glob.iglob(data_folder + '**.in', recursive=False):
            if os.path.isfile(filename):
                with open(filename, 'r') as inf:
                    input_data = inf.read()
                    with open(filename[:-3] + ".out", 'r') as outf:
                        output_data = outf.read()

                        # patch the input and assert the output
                        with patch('sys.stdin', StringIO(input_data)):
                            module.main()
                            res = mock_stdout.getvalue()
                            self.assertEqual(output_data, res, msg='failed {0} with output {1}'.format(filename[:-3], res))
                        mock_stdout.seek(0)
                        mock_stdout.truncate(0)
            assert True

    def test_2019_j1(self):
        from y2019 import j1
        self.check_question_data(j1, 'y2019/all_data/j1/')

    def test_2019_j2(self):
        from y2019 import j2
        self.check_question_data(j2, 'y2019/all_data/j2/')

    def test_2019_j3(self):
        from y2019 import j3
        self.check_question_data(j3, 'y2019/all_data/j3/')

if __name__ == '__main__':
    unittest.main()
