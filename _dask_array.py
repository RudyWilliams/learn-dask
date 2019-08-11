#esentially distributed numpy

#a blocked algorithm executes on a large dataset by breaking it into
#small blocks
import os
import h5py
import numpy as np 
import dask
import dask_decorators
import parallel
import nonparallel


#the block algs are hard-coded to run with a nice fitting dataset (e.g.
# one that has 1E9 observations). To get a fairer comparison with
# dask, it should have to figure out on its own. Not going to harp 
# on it now, but something to come back to.

@dask_decorators.runtime_timer
def block_sum(ds):
    """just an example of blocked alg"""
    sums = []
    for i in range(0, ds.len(), 1000000):
        chunk = ds[i:i+1000000]
        sums.append(chunk.sum())
    return sum(sums)

@dask_decorators.runtime_timer
def block_mean(ds):
    sums = []
    lens = []
    for i in range(0, ds.len(), 1000000):
        chunk = ds[i:i+1000000]
        #chunk is a numpy array
        sums.append(chunk.sum())
        lens.append(len(chunk))
    numerator = sum(sums)
    denominator = sum(lens) 
    #^this is what the solution has but it
    #seems unnec since sum(lens) = ds.len()
    return numerator / denominator

@dask_decorators.runtime_timer
def nonblock_sum(ds):
    return ds[:].sum()


@dask_decorators.runtime_timer
def nonblock_mean(ds):
    return ds[:].mean()


##introducing dask.array
## the above code chunks the data but it is still performed sequentially
from dask import array as da

@dask_decorators.runtime_timer
def da_sum(ds):
    dask_array = da.from_array(ds, chunks=(1000000,))
    sum_da = dask_array.sum()
    return sum_da.compute()


@dask_decorators.runtime_timer
def da_mean(ds):
    dask_array = da.from_array(ds, chunks=(1000000,))
    mean_da = dask_array.mean()
    return mean_da.compute()


if __name__ == '__main__':

    f = h5py.File(os.path.join('data', 'random.hdf5'), mode='r')
    dset = f['/x'] 
    #'/x' is just the name of the dataset (see build script)

    #nonblocking used bc it is a better way to compare
    #dask.array vs a traditional approach
    print(nonblock_sum(dset)) #sequential nonblocking
    print(block_sum(dset)) #sequential blocking
    print(da_sum(dset))

    ## the numbers do not match but that is probably due to 
    ## different rounding used???
    ## something to think about
    
    print(nonblock_mean(dset)) #sequential nonblocking
    print(block_mean(dset)) #sequential blocking
    print(da_mean(dset))
    ##see a performance boost and switched the order of calling
    ##bc not sure if that effects anything with runtime


