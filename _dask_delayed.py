""" Useful functions for playing with from the dask tutorial on github"""
import dask
from dask import delayed
import time

def inc(x):
    time.sleep(1)
    return x + 1

def add(x, y):
    time.sleep(1)
    return x + y

@delayed
def d_inc(x):
    time.sleep(1)
    return x + 1

@delayed
def d_add(x, y):
    time.sleep(1)
    return x + y

if __name__ == '__main__':

    #no parallelism
    t0 = time.time()
    x = inc(1)
    y = inc(2)
    z = add(x, y)
    t1 = time.time()
    elp_time = t1 - t0
    #shows that it runs in about 3 seconds
    print(f'sequential: {elp_time}')
    print(z)
    
    #parallelism
    d_t0 = time.time()
    x = d_inc(1)
    y = d_inc(2)
    z = d_add(x, y)
    d_t1 = time.time()
    d_elp_time = d_t1 - d_t0
    print(f'\ngraph build: {d_elp_time}')
    #no time bc no comp done
    
    comp_t0 = time.time()
    result = z.compute()
    comp_t1 = time.time()
    print(f'parallelism: {comp_t1 - comp_t0}')
    print(result)
    #does it in about two seconds
    #runs different threads to get performance boost
    
    #why we delay add as well
    """
    note the add is not delayed and so the timing seems to 
    do the impossible and get down to one second (if just timing compute)
    But, the z seems to execute x and y in parallel and then itself
    becomes delayed. In any case, it appears to run in 1 second because
    the execution is run and stopped so the timing of just compute is
    not accurate for the entire process"""

    print('\nWhy d_add is used...')
    d_t0 = time.time()
    x = d_inc(1)
    y = d_inc(2)
    z = add(x, y)
    d_t1 = time.time()
    d_elp_time = d_t1 - d_t0
    print(d_elp_time)
    #there is time... computation must of taken place
    
    print(z)
    comp_t0 = time.time()
    result = z.compute()
    comp_t1 = time.time()
    print(comp_t1 - comp_t0)
    print(result)

    
    print('\nWhat if z1 adds y and x??')
    #parallelism
    d_t0 = time.time()
    x = d_inc(1)
    y = d_inc(2)
    z = d_add(x, y)
    z1 = d_add(y, x)
    d_t1 = time.time()
    d_elp_time = d_t1 - d_t0
    print(f'graph build: {d_elp_time}')
    #no time bc no comp done
    
    comp_t0 = time.time()
    result = z.compute()
    result1 = z1.compute()
    comp_t1 = time.time()
    print(f'parallelism: {comp_t1 - comp_t0}')
    print(result)
    print(result1)
    """
    Takes 4 seconds because two seconds for each run of compute
    """

    print('\nInstead use dask.compute(z, z1)...')
    #parallelism
    d_t0 = time.time()
    x = d_inc(1)
    y = d_inc(2)
    z = d_add(x, y)
    z1 = d_add(y, x)
    d_t1 = time.time()
    d_elp_time = d_t1 - d_t0
    print(f'graph build: {d_elp_time}')
    #no time bc no comp done
    
    comp_t0 = time.time()
    result = dask.compute(z, z1)
    comp_t1 = time.time()
    print(f'parallelism: {comp_t1 - comp_t0}')
    print(result)