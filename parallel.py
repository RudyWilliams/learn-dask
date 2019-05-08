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
#   sumByOrigin
#   countByOrigin


if __name__ == '__main__':
    pass

   