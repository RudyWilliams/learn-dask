import pandas as pd 


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

if __name__ == '__main__':
    
    import time

    files = ['data\\florida_flights_2009.csv', 'data\\florida_flights_2019.csv']
    n_delayed = []
    n_flights = []

    t0 = time.time()
    for f in files:
        df = read_one(f)
        n_delayed.append(count_delayed(df))
        n_flights.append(count_flights(df))

    result = pct_delayed(n_delayed, n_flights)
    t1 = time.time()

    print(f'{result} in {t1 - t0} seconds')

