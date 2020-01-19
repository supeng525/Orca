import unittest
from setup.settings import *
from numpy.testing import *
from pandas.util.testing import *
import numpy as np
import dolphindb_numpy as dnp
import pandas as pd
import orca


class FunctionBitwiseAndTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # connect to a DolphinDB server
        orca.connect(HOST, PORT, "admin", "123456")

    def test_function_math_binary_bitwise_and_scalar(self):
        self.assertEqual(dnp.bitwise_and(1, 4), 0)
        self.assertEqual(np.bitwise_and(1, 4), 0)
        # self.assertEqual(dnp.bitwise_and(1, 4), np.bitwise_and(1, 4))

        self.assertEqual(dnp.bitwise_and(1, -5), 1)
        self.assertEqual(np.bitwise_and(1, -5), 1)
        # self.assertEqual(dnp.bitwise_and(1, -5), np.bitwise_and(1, -5))

        self.assertEqual(dnp.bitwise_and(0, 9), 0)
        self.assertEqual(np.bitwise_and(0, 9), 0)
        # self.assertEqual(dnp.bitwise_and(0, 9), np.bitwise_and(0, 9))

    def test_function_math_binary_bitwise_and_list(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 6, 9]
        assert_array_equal(dnp.bitwise_and(lst1, lst2), np.bitwise_and(lst1, lst2))

    def test_function_math_binary_bitwise_and_array_with_scalar(self):
        npa = np.array([1, 2, 3])
        dnpa = dnp.array([1, 2, 3])
        assert_array_equal(dnp.bitwise_and(dnpa, 1), np.bitwise_and(npa, 1))
        # TODO: bitwise_and bug
        # assert_array_equal(dnp.bitwise_and(1, dnpa), np.bitwise_and(1, npa))

    def test_function_math_binary_bitwise_and_array_with_array(self):
        npa1 = np.array([1, 2, 3])
        npa2 = np.array([4, 6, 9])

        dnpa1 = dnp.array([1, 2, 3])
        dnpa2 = dnp.array([4, 6, 9])
        assert_array_equal(dnp.bitwise_and(dnpa1, dnpa2), np.bitwise_and(npa1, npa2))

    def test_function_math_binary_bitwise_and_array_with_array_param_out(self):
        npa1 = np.array([1, 2, 3])
        npa2 = np.array([4, 6, 9])
        npa = np.zeros(shape=(1, 3))

        dnpa1 = dnp.array([1, 2, 3])
        dnpa2 = dnp.array([4, 6, 9])
        dnpa = dnp.zeros(shape=(1, 3))

        np.bitwise_and(npa1, npa2, out=npa)
        dnp.bitwise_and(dnpa1, dnpa2, out=dnpa)
        # TODO: dolphindb numpy bitwise_and bug
        # assert_array_equal(dnpa.to_numpy(), npa)

    def test_function_math_binary_bitwise_and_array_with_series(self):
        npa = np.array([1, 2, 3])
        dnpa = dnp.array([1, 2, 3])
        ps = pd.Series([4, 6, 9])
        os = orca.Series([4, 6, 9])
        assert_series_equal(dnp.bitwise_and(dnpa, os).to_pandas(), np.bitwise_and(npa, ps))
        assert_series_equal(dnp.bitwise_and(os, dnpa).to_pandas(), np.bitwise_and(ps, npa))

        pser = pd.Series([1, 2, 3])
        oser = orca.Series([1, 2, 3])
        assert_series_equal(dnp.bitwise_and(os, oser).to_pandas(), np.bitwise_and(ps, pser))

    def test_function_math_binary_bitwise_and_array_with_dataframe(self):
        npa = np.array([1, 2, 3])
        dnpa = dnp.array([1, 2, 3])
        pdf = pd.DataFrame({'A': [4, 6, 9]})
        odf = orca.DataFrame({'A': [4, 6, 9]})
        # TODO: orca bitwise_and bug
        # assert_frame_equal(odf.bitwise_and(dnpa, axis=0).to_pandas(), pdf.bitwise_and(npa, axis=0))


if __name__ == '__main__':
    unittest.main()
