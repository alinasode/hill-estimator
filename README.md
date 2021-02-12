# The Hill Estimator


Python implementation of the Hill Estimator and its corresponding Hill Plot within a specified zoomed window, avaliable in the following jypitor notebook

```
hill_estimator.ipynb
```


## Very short intuition behind code ##

Given the sorted order statistics <img src="https://render.githubusercontent.com/render/math?math=Y_{(1)} \leq ... \leq Y_{(n)}"> of a sample, the Hill estimator is defined by

<img src="https://render.githubusercontent.com/render/math?math=\kappa_n^{(k)} = \Big( k^{-1} \sum_{i=1}^{k} \log{\frac{Y_{(n-i+1)}}{Y_{(n-k)}}} \Big)^{-1} = \Big( \frac{1}{k} \sum_{i=1}^{k} \log{Y_{(n-i %2B 1)}} - \log Y_{(n-k)} \Big)^{-1}, \quad k=1,2,...,n-1">

where _k_ is the number of upper order statistics in the sample used for the estimation and _n_ is the number of observed sample values. With increasing _k_ the Hill estimator is stabilizing. And the question is which _k_ gives a reasonable estimation of <img src="https://render.githubusercontent.com/render/math?math=\kappa">. One might say that a good approximation of <img src="https://render.githubusercontent.com/render/math?math=\kappa"> lies a region where the graph is stable. 

For more information about the Hill Estimator and in general about heavy-tailed time series analysis I recommend taking a look at this PhD Thesis [[1]](#1).

## How to run existing code ##

* __Step 1__: Open `hill_estimator.ipynb`.
* __Step 2__: Load time series data, here S&P 500 Stock Index data, and split into *gains* and *losses*.
* __Step 3__: Run code from `utils/functions.py` and plot the Hill plot within some specified zoomed window range. 


- - - -

Get access to some time series data, apply the algorithm for the Hill estimator, and try out different zoomed windows and see what fit the data the best. Cheers!


## References ##

<a id="1">[1]</a> 
Xiaolei Xie. _Analysis of Heavy-Tailed Time Series_. PhD Thesis, School of the
Faculty of Science, University of Copenhagen (2017). [Link](http://web.math.ku.dk/noter/filer/phd17xx.pdf "Named link title")
