Covers my journey as I learn parallel computing in [Dask](https://dask.org/) so some of this might be rough around the edges. Started with direction 
from the Dask tutorial (only the free part) on [DataCamp](https://www.datacamp.com). Some files are based around the free DataCamp tutorial but most 
will be based around the free Dask tutorials at [the Dask GitHub tutorials page](https://github.com/dask/dask-tutorial).

The timing that I do for the functions does not use the timeit module so garbage collection is included and onluy single runs are considered. However, 
as I've continued to run the programs, I continue to see the imporvement of using parallel exection with Dask. You will also notice that I finally 
write a decorator to time my code. This is because decorators tend to intimidate me so I finally got around to relearning the material. 

## Modules
#### parallel.py
Where I'll write my functions that utilize dask for parallel computing.
#### dask_flights.py
Using dask.delayed() to get the code to run in parallel. From the DataCamp tutorial and the dask tutorial on GitHub.
#### flights.py
Using pandas in a traditional manner to compare the difference in runtimes.
#### _dask_delayed.py & _dask_for.py & _dask_control_flow.py
Messing around with tutorial on dask.delayed().
#### dask_decorators.py
Where I'll store decorators that become useful during tutorial. Right now, just a homemade timing wrapper.
#### dask_delay_groupby.py
Program to read three csv files and groupby origin airport summing the delayed minutes and counting the number of delayed flights. This deviates from the tutorial a bit because different data was used so more thought had to be put into cleaning.


