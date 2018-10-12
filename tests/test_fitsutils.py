import os
import unittest
import despyfitsutils.fitsutils as utils


TESTDIR = os.path.dirname(__file__)


class MefTest(unittest.TestCase):
    """Tests for a MEF object.
    """

    def setUp(self):
        inputs = [os.path.join(TESTDIR, 'data/input.fits.fz')]
        output = os.path.join(TESTDIR, 'data/output.fits.fz')

        # Instantiation of the class creates the output file (__init__()
        # calls write()) so clobber must be set to True.
        self.mef = utils.makeMEF(filenames=inputs, outname=output,
                                 clobber=True)

    def tearDown(self):
        try:
            os.remove(self.mef.outname)
        except FileNotFoundError:
            pass

    def testRead(self):
        self.mef.read()
        self.assertEqual(len(self.mef.HDU), 1)

    def testWrite(self):
        self.mef.write()
        self.assertTrue(os.path.isfile(self.mef.outname))
