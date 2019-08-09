import glob
from dask import delayed
import pandas as pd 
import dask_decorators

@delayed
def d_read_one(filename):
    return pd.read_csv(filename)

@delayed
def d_count_flights(df):
    return df.shape[0]

@delayed
def d_count_delayed(df):
    """
        count the number of delayed flights
    """
    return (df['DEP_DELAY'] > 0).sum()

@delayed
def d_pct_delayed(n_delayed, n_flights):
    return 100 * sum(n_delayed) / sum(n_flights)
    #n_delayed and n_flights will be lists for each
    #with elements corresponding to the chunks

@dask_decorators.runtime_timer
def parallel_main():
    
    files = glob.glob('data\\flights_20*.csv')
    n_delayed = []
    n_flights = []

    for file in files:
        df=d_read_one(file)
        n_delayed.append(d_count_delayed(df))
        n_flights.append(d_count_flights(df))
    
    results = d_pct_delayed(n_delayed, n_flights).compute()
    
    return results


if __name__ == '__main__':
    
    print(parallel_main())

    """
    We see a decrease from about 3.6 seconds to 1.9 seconds. But 
    I want to look into the delaying of the pct_delayed function
    and what it does.
    """ 