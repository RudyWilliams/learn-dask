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

def pct_delayed(n_delayed, n_flights):
    return 100 * sum(n_delayed) / sum(n_flights)


@dask_decorators.runtime_timer
def parallel_main():
    
    files = glob.glob('data\\flights_20*.csv')
    n_delayed = []
    n_flights = []

    for file in files:
        df=d_read_one(file)
        n_delayed.append(d_count_delayed(df))
        n_flights.append(d_count_flights(df))
    
    results = d_pct_delayed(n_delayed, n_flights)
    computed_results = results.compute()

    return results, computed_results


@dask_decorators.runtime_timer
def parallel_main_eager_pct():
    
    files = glob.glob('data\\flights_20*.csv')
    n_delayed = []
    n_flights = []

    for file in files:
        df=d_read_one(file)
        n_delayed.append(d_count_delayed(df))
        n_flights.append(d_count_flights(df))
    
    results = pct_delayed(n_delayed, n_flights)
    computed_results = results.compute()
    return results, computed_results


if __name__ == '__main__':
    
    graph0, r0 = parallel_main()
    graph0.visualize(filename='delayed_pct.png')
    print(r0)

    """
    We see a decrease from about 3.6 seconds to 1.9 seconds. But 
    I want to look into the delaying of the pct_delayed function
    and what it does.
    """ 
    print('\n')
    graph, r = parallel_main_eager_pct()
    graph.visualize(filename='eager_pct.png')
    print(r)
    """
    If take out compute() then we return a delayed true division object.
    The results appear to be the same. And doesn't appear to be doing any
    of the computation since the sums get delayed objects.
    """

    ### Note: Be mindful that there is no dask.delayed decorator
    ###       wrapping a function with a delayed function in it
    ###       This would delay a function that just builds a graph
    ###         -> is that what happens with d_pct_delayed() if it 
    ###            seems that the functions within become implicitly 
    ###            delayed... something to think about
    ###            The graphs are different so I will have to study
    ###            those to see what's happenning