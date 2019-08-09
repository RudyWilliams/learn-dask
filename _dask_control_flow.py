import dask
from dask import delayed
import time
from _dask_delayed import inc, d_inc 

def double(x):
    time.sleep(1)
    return 2 * x

@delayed
def d_double(x):
    time.sleep(1)
    return 2 * x

def is_even(x):
    return not x % 2 #if even -> 0 not -> 1

@delayed
def d_is_even(x):
    return not x % 2


data = list(range(1,11))

t0 = time.time()
results = [double(x) if is_even(x) else inc(x) for x in data]
total = sum(results)
t1 = time.time()
print(f'{total} in {t1 - t0} seconds.')

#now delay it (properly)
t0 = time.time()
results = [d_double(x) if is_even(x) else d_inc(x) for x in data]
#print(results)
total = sum(results)
total = total.compute()
t1 = time.time()
print(f'{total} in {t1 - t0} seconds.\n')
#cuts 10s to 2s
"""
If we were to print 'results' we would see that the proper delayed functions
are called (e.g. [d_inc, d_double, d_inc, ..., d_double]).
"""


#now delay it (delaying the if)
# t0 = time.time()
# results = [d_double(x) if d_is_even(x) else d_inc(x) for x in data]
# total = sum(results)
# total = total.compute()
# t1 = time.time()
# print(f'{total} in {t1 - t0} seconds.')
## results in an error: Cannot get truth value of delayed object
## i.e. dask doesn't know what delayed function to give the elements