import unittest
from setup.settings import *
from numpy.testing import *
from pandas.util.testing import *
import numpy as np
import dolphindb_numpy as dnp
import pandas as pd
import orca


class FunctionDivideTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # connect to a DolphinDB server
        orca.connect(HOST, PORT, "admin", "123456")

    def test_function_math_binary_divide_scalar(self):
        self.assertEqual(dnp.divide(1.2 + 1j, 1.2 - 1j), np.divide(1.2 + 1j, 1.2 - 1j))
        self.assertEqual(dnp.divide(0.5, 9), np.divide(0.5, 9))
        self.assertEqual(dnp.divide(-1, 8.5), np.divide(-1, 8.5))
        self.assertEqual(dnp.divide(1, 4), np.divide(1, 4))
        self.assertEqual(dnp.divide(1, -5), np.divide(1, -5))
        self.assertEqual(dnp.divide(0, 9), np.divide(0, 9))

        self.assertEqual(dnp.isnan(dnp.divide(dnp.nan, -5)), True)
        self.assertEqual(np.isnan(np.divide(dnp.nan, -5)), True)

    def test_function_math_binary_divide_list(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 6, 9]
        assert_array_equal(dnp.divide(lst1, lst2), np.divide(lst1, lst2))

    def test_function_math_binary_divide_array_with_scalar(self):
        npa = np.array([1, 2, 3])
        dnpa = dnp.array([1, 2, 3])
        assert_array_equal(dnp.divide(dnpa, 1), np.divide(npa, 1))
        assert_array_equal(dnp.divide(dnpa, dnp.nan), np.divide(npa, np.nan))
        # TODO: divide bug
        # assert_array_equal(dnp.divide(1, dnpa), np.divide(1, npa))

    def test_function_math_binary_divide_array_with_array(self):
        npa1 = np.array([1, 2, 3])
        npa2 = np.array([4, 6, 9])

        dnpa1 = dnp.array([1, 2, 3])
        dnpa2 = dnp.array([4, 6, 9])
        assert_array_equal(dnp.divide(dnpa1, dnpa2), np.divide(npa1, npa2))

    def test_function_math_binary_divide_array_with_array_param_out(self):
        npa1 = np.array([1, 2, 3])
        npa2 = np.array([4, 6, 9])
        npa = np.zeros(shape=(1, 3))

        dnpa1 = dnp.array([1, 2, 3])
        dnpa2 = dnp.array([4, 6, 9])
        dnpa = dnp.zeros(shape=(1, 3))

        np.divide(npa1, npa2, out=npa)
        dnp.divide(dnpa1, dnpa2, out=dnpa)
        # TODO: dolphindb numpy divide bug
        # assert_array_equal(dnpa.to_numpy(), npa)

    def test_function_math_binary_divide_array_with_series(self):
        npa = np.array([1, 2, 3])
        dnpa = dnp.array([1, 2, 3])
        ps = pd.Series([4, 6, 9])
        os = orca.Series([4, 6, 9])
        assert_series_equal(dnp.divide(dnpa, os).to_pandas(), np.divide(npa, ps))
        assert_series_equal(dnp.divide(os, dnpa).to_pandas(), np.divide(ps, npa))

    def test_function_math_binary_divide_array_with_dataframe(self):
        npa = np.array([1, 2, 3])
        dnpa = dnp.array([1, 2, 3])
        pdf = pd.DataFrame({'A': [4, 6, 9]})
        odf = orca.DataFrame({'A': [4, 6, 9]})
        # TODO: orca divide bug
        # assert_frame_equal(odf.divide(dnpa, axis=0).to_pandas(), pdf.divide(npa, axis=0))


if __name__ == '__main__':
    unittest.main()
