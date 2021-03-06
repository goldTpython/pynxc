import unittest
import glob

import os

import sys
sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0] + '/../../')))

from pynxc import python_to_nxc

class TextConversion(unittest.TestCase):

    def test_directories(self):
        mypath = os.path.dirname(os.path.abspath(sys.argv[0]))
        inputs = glob.glob(mypath + '/in/*.py')

        print("Running tests on inputs %s" % inputs)

        for input in inputs:
            if os.path.basename(input).startswith('_'):
                continue

            nxc_filename = input.replace('.py', '.nxc')
            python_to_nxc(input, nxc_filename, dry=True)

            testfile = nxc_filename.replace('tests/in/', 'tests/out/')

            print("Testing %s" % input)
            self.assertEqual(open(nxc_filename, 'r').read(),
                                open(testfile, 'r').read())


if __name__ == '__main__':
    unittest.main()

