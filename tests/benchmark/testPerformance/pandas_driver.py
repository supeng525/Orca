import pandas as pd
from columns import value_columns, ticker_columns


class PandasDriver(object):
    def __init__(self, ticker_file, value_file):
        self.ticker_file = ticker_file
        self.value_file = value_file

        self.df_ticker = None
        self.df_value = None

    def a_load(self):
        self.df_ticker = pd.read_csv(self.ticker_file, parse_dates=[0])
        self.df_ticker.columns = ticker_columns

        self.df_value = pd.read_csv(self.value_file)
        self.df_value.columns = value_columns

    def groupby(self):
        self.df_ticker.groupby("type").agg({'svalue': 'mean', 'price': 'sum'})

    def filter(self):
        _ = self.df_ticker[self.df_ticker['type'] == 'a']

    def select(self):
        _ = self.df_ticker[["ticker", "type"]]

    def sort(self):
        self.df_ticker.sort_values(by='ticker')

    def join(self):
        joined = self.df_ticker.merge(self.df_value, on='type')
        joined['total'] = joined['value'] + joined['svalue']

    def resample_ms(self):
        self.df_ticker.resample('ms', on='date')['svalue'].mean()

    def resample_3ms(self):
        self.df_ticker.resample('3ms', on='date')['svalue'].mean()

    def resample_S(self):
        self.df_ticker.resample('S', on='date')['svalue'].mean()

    def resample_3S(self):
        self.df_ticker.resample('3S', on='date')['svalue'].mean()

    def resample_T(self):
        self.df_ticker.resample('T', on='date')['svalue'].mean()

    def resample_3T(self):
        self.df_ticker.resample('3T', on='date')['svalue'].mean()

    def resample_H(self):
        self.df_ticker.resample('H', on='date')['svalue'].mean()

    def resample_3H(self):
        self.df_ticker.resample('3H', on='date')['svalue'].mean()

    def resample_D(self):
        self.df_ticker.resample('D', on='date')['svalue'].mean()

    def resample_3D(self):
        self.df_ticker.resample('3D', on='date')['svalue'].mean()

    def resample_W(self):
        self.df_ticker.resample('W', on='date')['svalue'].mean()

    def resample_M(self):
        self.df_ticker.resample('M', on='date')['svalue'].mean()

    def resample_3M(self):
        self.df_ticker.resample('3M', on='date')['svalue'].mean()

    def resample_Q(self):
        self.df_ticker.resample('Q', on='date')['svalue'].mean()

    def resample_3Q(self):
        self.df_ticker.resample('3Q', on='date')['svalue'].mean()

    def resample_A(self):
        self.df_ticker.resample('A', on='date')['svalue'].mean()

    def resample_3A(self):
        self.df_ticker.resample('3A', on='date')['svalue'].mean()

        self.df_ticker.resample('3A', on='date')['svalue'].mean()

