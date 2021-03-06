import unittest
from unittest.mock import patch
import io
from io import StringIO

class TestAllYears(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def check_question_data(self, module, data_folder, mock_stdout):
        import glob, os

        mock_stdout.seek(0)
        mock_stdout.truncate(0)

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
                            self.assertEqual(output_data, res,
                                             msg='failed {0} with output {1}'.format(filename[:-3], res))
                        mock_stdout.seek(0)
                        mock_stdout.truncate(0)
            assert True

    def check_question_runs_only(self, module, data_folder):
        import glob, os

        # for each input test
        for filename in glob.iglob(data_folder + '**.in', recursive=False):
            if os.path.isfile(filename):
                print("testing " + filename)
                with open(filename, 'r') as inf:
                    input_data = inf.read()

                    # patch the input and assert the output
                    with patch('sys.stdin', StringIO(input_data)):
                        module.main()

            assert True

    def test_2019_s3(self):
       from y2019 import s3
       self.check_question_runs_only(s3, 'y2019/all_data/s3/')


    def test_2019_j1(self):
        from y2019 import j1
        self.check_question_data(j1, 'y2019/all_data/j1/')

    def test_2019_j2(self):
        from y2019 import j2
        self.check_question_data(j2, 'y2019/all_data/j2/')

    def test_2019_j3(self):
        from y2019 import j3
        self.check_question_data(j3, 'y2019/all_data/j3/')

    def test_2019_j4(self):
        from y2019 import j4
        self.check_question_data(j4, 'y2019/all_data/s1_j4/')

    def test_2019_s2(self):
        from y2019 import s2
        self.check_question_data(s2, 'y2019/all_data/s2/')

    def test_2019_j5(self):
        from y2019 import j5
        self.check_question_runs_only(j5, 'y2019/all_data/j5/')

if __name__ == '__main__':
    unittest.main()
