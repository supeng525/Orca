import unittest
from setup.settings import *
from numpy.testing import *
from pandas.util.testing import *
import numpy as np
import dolphindb_numpy as dnp
import pandas as pd
import orca


class FunctionLogicalAndTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # connect to a DolphinDB server
        orca.connect(HOST, PORT, "admin", "123456")

    def test_function_math_binary_logical_and_scalar(self):
        self.assertEqual(dnp.logical_and(1.2 + 1j, 1.2 - 1j), np.logical_and(1.2 + 1j, 1.2 - 1j))
        self.assertEqual(dnp.logical_and(0.5, 9), np.logical_and(0.5, 9))
        self.assertEqual(dnp.logical_and(-1, 8.5), np.logical_and(-1, 8.5))
        self.assertEqual(dnp.logical_and(1, 4), np.logical_and(1, 4))
        self.assertEqual(dnp.logical_and(1, -5), np.logical_and(1, -5))
        self.assertEqual(dnp.logical_and(0, 9), np.logical_and(0, 9))
        self.assertEqual(dnp.logical_and(dnp.nan, -5), np.logical_and(dnp.nan, -5))

    def test_function_math_binary_logical_and_list(self):
        lst1 = [0, 1, 2]
        lst2 = [4, 6, 9]
        assert_array_equal(dnp.logical_and(lst1, lst2), np.logical_and(lst1, lst2))

    def test_function_math_binary_logical_and_array_with_scalar(self):
        npa = np.array([0, 1, 2])
        dnpa = dnp.array([0, 1, 2])
        assert_array_equal(dnp.logical_and(dnpa, 1), np.logical_and(npa, 1))
        assert_array_equal(dnp.logical_and(dnpa, dnp.nan), np.logical_and(npa, np.nan))
        assert_array_equal(dnp.logical_and(1, dnpa), np.logical_and(1, npa))

    def test_function_math_binary_logical_and_array_with_array(self):
        npa1 = np.array([0, 1, 2])
        npa2 = np.array([4, 6, 9])

        dnpa1 = dnp.array([0, 1, 2])
        dnpa2 = dnp.array([4, 6, 9])
        assert_array_equal(dnp.logical_and(dnpa1, dnpa2), np.logical_and(npa1, npa2))

    def test_function_math_binary_logical_and_array_with_array_param_out(self):
        npa1 = np.array([0, 1, 2])
        npa2 = np.array([4, 6, 9])
        npa = np.zeros(shape=(1, 3))

        dnpa1 = dnp.array([0, 1, 2])
        dnpa2 = dnp.array([4, 6, 9])
        dnpa = dnp.zeros(shape=(1, 3))

        np.logical_and(npa1, npa2, out=npa)
        dnp.logical_and(dnpa1, dnpa2, out=dnpa)
        assert_array_equal(dnpa, npa)

    def test_function_math_binary_logical_and_array_with_series(self):
        npa = np.array([0, 1, 2])
        dnpa = dnp.array([0, 1, 2])
        ps = pd.Series([4, 6, 9])
        os = orca.Series([4, 6, 9])
        assert_series_equal(dnp.logical_and(dnpa, os).to_pandas(), np.logical_and(npa, ps))
        assert_series_equal(dnp.logical_and(os, dnpa).to_pandas(), np.logical_and(ps, npa))

        pser = pd.Series([1, 2, 4])
        oser = orca.Series([1, 2, 4])
        assert_series_equal(dnp.logical_and(os, oser).to_pandas(), np.logical_and(ps, pser))

    def test_function_math_binary_logical_and_array_with_dataframe(self):
        npa = np.array([1])
        dnpa = dnp.array([1])
        pdf = pd.DataFrame({'A': [4, 6, 9]})
        odf = orca.DataFrame({'A': [4, 6, 9]})
        assert_frame_equal(dnp.logical_and(odf, dnpa).to_pandas(), np.logical_and(pdf, npa))
        assert_frame_equal(dnp.logical_and(dnpa, odf).to_pandas(), np.logical_and(npa, pdf))

        pdfrm = pd.DataFrame({'A': [0, 7, 1]})
        odfrm = orca.DataFrame({'A': [0, 7, 1]})
        assert_frame_equal(dnp.logical_and(odf, odfrm).to_pandas(), np.logical_and(pdf, pdfrm))


if __name__ == '__main__':
    unittest.main()
