Covers my journey as I learn parallel computing in [Dask](https://dask.org/) so some of this might be rough around the edges. Started with direction 
from the Dask tutorial (only the free part) on [DataCamp](https://www.datacamp.com). Some files are based around the free DataCamp tutorial but most 
will be based around the free Dask tutorials at [the Dask GitHub tutorials page](https://github.com/dask/dask-tutorial).

The timing that I do for the functions does not use the timeit module so garbage collection is included and only single runs are considered. However, 
as I've continued to run the programs, I continue to see the imporvement of using parallel exection with Dask. The timing is done with the use of decorators written in the dask_decorators.py file. 

## Modules
#### data
This folder holds the data for the excercises. Note, flights_2020.csv, flights_2021.csv, and flights_2022.csv are duplicates of the flight records from 2017-2019 in order to increase the workload for the programs. 
#### parallel.py
Where I'll write my functions that utilize dask for parallel computing.
#### dask_flights.py
Using dask.delayed() to get the code to run in parallel. From the DataCamp tutorial and the dask tutorial on GitHub.
#### flights.py
Using pandas in a traditional manner to compare the difference in runtimes.
#### _dask_delayed.py & _dask_for.py & _dask_control_flow.py
Messing around with tutorial on dask.delayed(). Taking what they cover and experimenting a bit.
#### dask_decorators.py
Where I'll store decorators that become useful during tutorial. Right now, just some homemade timing wrappers.
#### dask_delay_groupby.py
Program to read three csv files and groupby origin airport summing the delayed minutes and counting the number of delayed flights. This deviates from the tutorial a bit because different data was used so more thought had to be put into cleaning.


