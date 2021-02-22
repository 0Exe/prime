# prime

## installation

download `prime.py` and put in folder of use

## usage

```py
from prime import prime
from prime import *

prime(integer) # returns True / False

# -- other uses --

for i in range(num1, num2):
  prime(i)
  
for i in range(num1, num2):
  placeholder = prime(i)
  if placeholder:
    print(placeholder)
  # doesn't give back False, only True
  ```
  
 ```py
import prime

prime.prime(integer) # returns True / False

# -- other uses --

for i in range(num1, num2):
  prime.prime(i)
  
for i in range(num1, num2):
  placeholder = prime.prime(i)
  if placeholder:
    print(placeholder)
  # doesn't give back False, only True
  ```
