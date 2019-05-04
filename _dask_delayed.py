""" Useful functions for playing with from the dask tutorial on github"""

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

    '''
    t0 = time.time()
    x = inc(1)
    y = inc(2)
    z = add(x, y)
    t1 = time.time()
    elp_time = t1 - t0
    #shows that it runs in about 3 seconds
    print(elp_time)
    '''

    d_t0 = time.time()
    x = d_inc(1)
    y = d_inc(2)
    z = d_add(x, y)
    d_t1 = time.time()
    d_elp_time = d_t1 - d_t0
    #print(d_elp_time)
    #no time bc no comp done
    

    comp_t0 = time.time()
    z.compute()
    comp_t1 = time.time()
    print(comp_t1 - comp_t0)
    #does it in about two seconds
    #runs different threads to get performance boost
