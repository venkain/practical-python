# bounce.py
#
# Exercise 1.5

height = 100.0
bounce = 0.6

for count in range(1, 11):
    height *= bounce
    print(count, round(height,4))
