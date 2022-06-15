Dynamic programming is a technique for computing a recursive 
algorithm with a highly overlapping sub-problem structure. 
Dynamic programming achieves efficiency by solving each sub problem
only once. 

The first technique for avoiding a repeated work is memoization,
which caches the results of repeated calculations. 
This trades off speed at the expense of memory usage. 

The other technique is bottom-up dynamic programming, 
which represents recursive problems as directed acyclic graphs. 
The DAG representation can be traversed in order of dependency,
solving sub-problems before they are needed. 
And finally, by throwing away under needed results, problems can be solved with both minimal time and space.
In turn this results in efficient time and space complexity. 

