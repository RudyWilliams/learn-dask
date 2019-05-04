#for loops are good candidates for parallelizing
from dask import delayed
from _dask_delayed import inc, d_inc
from time import time

data = [1, 2, 3, 4, 5, 6, 7, 8]

def run_for_inc(delay=True):
    """run the for loop with append with either parallel computing
       or no parallel computing (delay=False).
    """
    if delay:
        func = d_inc
    else:
        func = inc
    
    t0 = time()
    results = []
    for x in data:
        y = func(x)
        results.append(y)
    total = sum(results)
    if delay: #don't like that checking if delay twice
        total = total.compute()
    t1 = time()

    return total, t1 - t0

def run_list_comp_inc(delay=True):
    """run list comprehension to to build results with either parallel
       computing or no parallel computing (delay=False).
    """    
    if delay:
        func = d_inc
    else:
        func = inc
    
    t0 = time()
    results = [func(x) for x in data]
    total = sum(results)
    if delay:
        total = total.compute()
    t1 = time()

    return total, t1 - t0




if __name__ == '__main__':
    tot, elpsd_t = run_for_inc(delay=False)
    print(f'NO PARALLEL COMPUTE: total={tot} in {elpsd_t} seconds.')
    par_tot, par_elpsd_t = run_for_inc(delay=True)
    print(f'PARALLEL COMPUTE: total={par_tot} in {par_elpsd_t} seconds.\n')
    ## we see a significant speed up from 8 seconds to 1 second

    tot_lc, elpsd_t_lc = run_list_comp_inc(delay=False)
    print(f'LIST COMP, NO PARALLEL COMPUTE: total={tot_lc} in {elpsd_t_lc} seconds.')
    par_tot_lc, par_elpsd_t_lc = run_list_comp_inc(delay=True)
    print(f'LIST COMP, PARALLEL COMPUTE: total={par_tot_lc} in {par_elpsd_t_lc} seconds.')
    ## seemingly no speedup using a list comp bc the number of times we 
    ## append is only eight