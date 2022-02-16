```python
import math

a, b = 0, math.pi
```


```python
import random
import math

def f1(x):
    return math.log(x) / x

def f(x): return math.sin(x)

def monte_carlo_method(f, a, b, n = 10_000):
    count = 0
    for i in range(n):
        x, y = random.uniform(a, b), random.uniform(0, 1)        
        if y <= f(x): count += 1
    
    area = math.pi*1
    return count/n * area
```


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(a, b, 0.1)
y = [f(i) for i in x]
plt.plot(x, y)
plt.fill_between(x, y, 0, alpha=0.2)
plt.show()

```


    
![png](notebook_1_files/notebook_1_2_0.png)
    



```python
monte_carlo_method(f, a, b, 1_000_000)
```




    2.000138945205092




```python
%%html
<iframe src="https://www.wolframalpha.com/input/?i=integral+of+sinx+from+0+to+pi" width="800" height="400"></iframe>
```


<iframe src="https://www.wolframalpha.com/input/?i=integral+of+sinx+from+0+to+pi" width="800" height="400"></iframe>


