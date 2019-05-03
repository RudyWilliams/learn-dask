from dask import delayed
import pandas as pd 

@delayed
def read_one(filename):
    return pd.read_csv(filename)

@delayed
def count_flights(df):
    return df.shape[0]

@delayed
def count_delayed(df):
    """
        count the number of delayed flights
    """
    return (df['DEP_DELAY'] > 0).sum()

@delayed
def pct_delayed(n_delayed, n_flights):
    return 100 * sum(n_delayed) / sum(n_flights)
    #n_delayed and n_flights will be lists for each
    #with elements corresponding to the chunks

if __name__ == '__main__':
    files = ['data\\florida_flights_2009.csv', 'data\\florida_flights_2019.csv']
    n_delayed = []
    n_flights = []

    for f in files:
        df = read_one(f)
        n_delayed.append(count_delayed(df))
        n_flights.append(count_flights(df))

    #compute them together
    result = pct_delayed(n_delayed, n_flights)
    print(result.compute())

