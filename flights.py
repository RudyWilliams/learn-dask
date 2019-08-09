import pandas as pd 
import dask_decorators  

def read_one(filename):
    return pd.read_csv(filename)

def count_flights(df):
    return df.shape[0]

def count_delayed(df):
    """
        count the number of delayed flights
    """
    return (df['DEP_DELAY'] > 0).sum()

def pct_delayed(n_delayed, n_flights):
    return 100 * sum(n_delayed) / sum(n_flights)
    #n_delayed and n_flights will be lists for each
    #with elements corresponding to the chunks

@dask_decorators.runtime_timer
def main():
    n_delayed = []
    n_flights = []

    for file in files:
        df=read_one(file)
        n_delayed.append(count_delayed(df))
        n_flights.append(count_flights(df))
    
    results = pct_delayed(n_delayed, n_flights)
    
    return results

if __name__ == '__main__':
    
    import glob

    files = glob.glob('data\\flights_20*.csv')
    print(main())    
