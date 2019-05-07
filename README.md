Covers my journey as I learn parallel computing in [Dask](https://dask.org/) so some of this might be rough around the edges. Started with direction 
from the Dask tutorial (only the free part) on [DataCamp](https://www.datacamp.com). Some files are based around the free DataCamp tutorial but most 
will be based around the free Dask tutorials at [the Dask GitHub tutorials page](https://github.com/dask/dask-tutorial).

The timing that I do for the functions does not use the timeit module so garbage collection is included and onluy single runs are considered. However, 
as I've continued to run the programs, I continue to see the imporvement of using parallel exection with Dask. You will also notice that I finally 
write a decorator to time my code. This is because decorators tend to intimidate me so I finally got around to relearning the material. 
