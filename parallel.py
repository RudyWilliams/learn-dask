"""
    Module to contain the functions for parallel computing
"""
from dask import delayed
import pandas as pd

@delayed
def csv_to_df(*args, **kwargs):
    return pd.read_csv(*args, **kwargs)

#all methods on df will be delayed too
#Won't need sep parallel functions:
#   dropping nans
#   groupby 
#   sumByOrigin?
#   countByOrigin?






if __name__ == '__main__':
    df = csv_to_df(filepath_or_buffer='data\\flights_2017.csv', usecols=['YEAR', 'ORIGIN', 'ORIGIN_CITY_NAME', 'ORIGIN_STATE_ABR',
            'DEST', 'DEST_CITY_NAME', 'DEST_STATE_ABR', 'DEP_DELAY',
            'DEP_DELAY_NEW', 'ACTUAL_ELAPSED_TIME'])

   