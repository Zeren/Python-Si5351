# Python-Si5351
Python library for Si5351 
[Inspirited and derived from roseengineering/RasPi-Si5351.py ](https://github.com/roseengineering/RasPi-Si5351.py)

## Features
- Frequencies 8 kHz to 200 MHz
- Easy calculation of frequency
- Automatic switching between integer and fractional mode with preferences for integer mode
- Possibility of using one pll for two or more outputs with different output divider settings

## Usage
```Python
from copy import copy
synt = Si5351()
settings1 = synt.get_parameters(10e6)
synt.setup(SI5351_PLL_A, 0, settings1)
settings2 = copy(settings1)
settings2.d = 120
synt.setup(SI5351_PLL_A, 0, settings1)
synt.setup(SI5351_PLL_A, 1, settings2)
```
Output 0 is 10 MHz, Output 1 is 5 MHz
