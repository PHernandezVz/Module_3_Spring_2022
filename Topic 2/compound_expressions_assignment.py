"""
Open your Python shell, PyCharm, or Jupyter Notebook, and test making expressions.
Set MAX = 10, MIN = 0
Set a variable y to a value
Test whether y is above MAX
Test whether y is below MIN
Set a variable x to a value
Test whether it is between the MIN and MAX but does not equal MAX nor MIN
Test whether it is within MIN up to MAX but does not equal MAX
Test whether it is above MIN up to and including MAX
Submit a screenshot (or multiple screenshots if you can't get all on one screen) with all above.'
"""

MAX = 10
MIN = 0
y = 13

print(y > MAX)
print(y < MIN)

x = 5

print(MIN < x < MAX)
print(MIN <= x < MAX)
print(MIN < x <= MAX)
