import math
import os
import unittest
import despyfitsutils.fits_special_metadata as meta


TESTDIR = os.path.dirname(__file__)
TOLERANCE = 1.0e-02


class FuncBandTests(unittest.TestCase):
    """Test for func_band() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        band = meta.func_band(self.valid)
        self.assertEqual(band, 'g')

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            band = meta.func_band(self.invalid)


class FuncCamsymTest(unittest.TestCase):
    """Test for func_camsys() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        camsym = meta.func_camsym(self.valid)
        self.assertEqual(camsym, 'D')

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            cam = meta.func_camsym(self.invalid)


class FuncNiteTest(unittest.TestCase):
    """Test for func_nite() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        nite = meta.func_nite(self.valid)
        self.assertEqual(nite, '20150217')

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            nite = meta.func_nite(self.invalid)


class FuncObjectTest(unittest.TestCase):
    """Test for func_objects() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        obj = meta.func_objects(self.valid)
        self.assertEqual(obj, 3)

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            obj = meta.func_objects(self.invalid)


class FuncFieldTest(unittest.TestCase):
    """Test for func_field() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        with self.assertRaises(KeyError):
            field = meta.func_field(self.valid)

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            field = meta.func_field(self.invalid)


class FuncRadegTest(unittest.TestCase):
    """Test for func_radeg() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        e = 147.6202
        x = meta.func_radeg(self.valid)
        self.assertTrue(math.fabs(x - e) < math.fabs(x * TOLERANCE))

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            x = meta.func_radeg(self.invalid)


class FuncTradegTest(unittest.TestCase):
    """Test for func_tradeg() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        e = 147.6202
        x = meta.func_radeg(self.valid)
        self.assertTrue(math.fabs(x - e) < math.fabs(x * TOLERANCE))

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            x = meta.func_tradeg(self.invalid)


class FuncDecdegTest(unittest.TestCase):
    """Test for func_decdeg() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        e = -6.3013
        x = meta.func_decdeg(self.valid)
        self.assertTrue(math.fabs(x - e) < math.fabs(x * TOLERANCE))

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            x = meta.func_decdeg(self.invalid)


class FuncTdecdegTest(unittest.TestCase):
    """Test for func_tdecdeg() function.
    """

    def setUp(self):
        self.valid = os.path.join(TESTDIR, 'data/input.fits.fz')
        self.invalid = os.path.join(TESTDIR, 'data/notafile.fits.fz')

    def tearDown(self):
        pass

    def testFileExists(self):
        e = -6.3013
        x = meta.func_tdecdeg(self.valid)
        self.assertTrue(math.fabs(x - e) < math.fabs(x * TOLERANCE))

    def testFileMissing(self):
        with self.assertRaises(FileNotFoundError):
            x = meta.func_tdecdeg(self.invalid)
