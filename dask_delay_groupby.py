import os
import glob
from time import time
from dask import delayed, compute
import pandas as pd 
import parallel
import flights as non_parallel
from dask_decorators import runtime_timer


@delayed
def delayed_set(delayed_list):
    return set(delayed_list)

def make_index_consistent(series_list, parallel=False):
    """summing the series leads to nans staying nans...should be considered 0s"""
    assert len(series_list) == 3        
    airport_index = series_list[0].index.tolist() + series_list[1].index.tolist() + series_list[2].index.tolist()

    if parallel:
        airport_index = delayed_set(airport_index)
    else:
        airport_index = set(airport_index)
    
    return [s.reindex(index=airport_index, fill_value=0) for s in series_list]

@runtime_timer
def delays_and_count_per_airport(file_list):
    """
        calculate the sum of delay time and counts per airport.
        
        Args:
            file_list: list - the csv files to read in

        Returns:
            tuple of pandas series
    """
    sums = []
    counts = []
    #some files read in a blank col... ensures the columns will be consistent for each file
    cols = ['YEAR', 'ORIGIN', 'ORIGIN_CITY_NAME', 'ORIGIN_STATE_ABR',
            'DEST', 'DEST_CITY_NAME', 'DEST_STATE_ABR', 'DEP_DELAY',
            'DEP_DELAY_NEW', 'ACTUAL_ELAPSED_TIME']

    for f in file_list:
        df = pd.read_csv(f, usecols=cols)
        df = df.dropna(axis=0, subset=['DEP_DELAY'])
        
        groupByOrigin = df.groupby('ORIGIN')

        #get the sum of the dep delays by ORIGIN
        sumByOrigin = groupByOrigin['DEP_DELAY'].sum()
        countByOrigin = groupByOrigin['DEP_DELAY'].count()

        sums.append(sumByOrigin)
        counts.append(countByOrigin)


    #python's built in sum() would add the series as needed
    #BUT we need to fill in any nans first
    del_sums = make_index_consistent(sums)
    arpt_counts = make_index_consistent(counts)
    delays_by_airport_sum = sum(del_sums)
    delays_by_airport_count = sum(arpt_counts)

    return delays_by_airport_sum, delays_by_airport_count


@runtime_timer
def d_delays_and_count_per_airport(file_list):
    """
        use dask.delayed to make faster calculation of the sum of delay time and counts per airport.
        
        Args:
            file_list: list - the csv files to read in

        Returns:
            tuple of pandas series
    """
    sums = []
    counts = []
    #some files read in a blank col... ensures the columns will be consistent for each file
    cols = ['YEAR', 'ORIGIN', 'ORIGIN_CITY_NAME', 'ORIGIN_STATE_ABR',
            'DEST', 'DEST_CITY_NAME', 'DEST_STATE_ABR', 'DEP_DELAY',
            'DEP_DELAY_NEW', 'ACTUAL_ELAPSED_TIME']

    for f in file_list:
        df = parallel.csv_to_df(filepath_or_buffer=f, usecols=cols)
        df = df.dropna(axis=0, subset=['DEP_DELAY'])
        
        groupByOrigin = df.groupby('ORIGIN')

        #get the sum of the dep delays by ORIGIN
        sumByOrigin = groupByOrigin['DEP_DELAY'].sum()
        countByOrigin = groupByOrigin['DEP_DELAY'].count()

        sums.append(sumByOrigin)
        counts.append(countByOrigin)

    #python's built in sum() would add the series as needed
    #BUT we need to fill in any nans first
    del_sums = make_index_consistent(sums, parallel=True)
    arpt_counts = make_index_consistent(counts, parallel=True)
    delays_by_airport_sum = sum(del_sums)
    delays_by_airport_count = sum(arpt_counts)
    all_years_sums, all_years_counts = compute(delays_by_airport_sum, delays_by_airport_count)
    
    return all_years_sums, all_years_counts

#leave out the florida only data files
files = [f for f in glob.glob('data\\*.csv') if 'florida' not in f]

print('IN PARALLEL...')
sums, counts = d_delays_and_count_per_airport(files)

print(sums)
print(counts)

print('NON-PARALLEL...')
sums, counts = delays_and_count_per_airport(files)

print(sums)
print(counts)


    

    

