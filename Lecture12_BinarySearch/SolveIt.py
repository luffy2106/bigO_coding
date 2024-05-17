"""
1. Question
https://bigocoder.com/courses/138/lectures/1843/problems/1077?view=statement

2. Solution
Since we know that x in [0,1], so we can use binary search to reduce searching space


f'(x) = -pe^-x + qcos(x) - rsin(x) + sec^2(x) + 2t*x
with 
- 0<= p,r <=20
- -20<= q,s,t <=0
- 0<=x<=1

Considering the given ranges of coefficients and the domain of (x), let's break it down:

1. Exponential Term:
- Since (p) is between 0 and 20, the exponential term (-pe^{-x}) will be negative for all (x) within the domain ([0,1]).

2. Trigonometric Terms:
Considering the ranges of (q) and (r):
- (qcos(x)) may vary in sign within the domain ([0,1]) depending on the value of (q).
- (-rsin(x)) may vary in sign within the domain ([0,1]) depending on the value of (r).

3. Linear Term:
- The linear term (2t*x) will be non-negative within the domain ([0,1]) since (t) is in the range ([-20,0]).

4. Secant Term:
- The secant term (sec^2(x)) will be non-negative for all (x) within the domain ([0,1]).

Considering the signs of each component of the derivative within the specified domain, the overall derivative (f'(x)) may change in sign due to the trigonometric terms based on the specific values of (q) and (r). However, the exponential term and the secant term ensure that the derivative does not become positive throughout the domain.
Therefore, based on the given ranges of coefficients and domain, the function represented by the expression (pe^{-x} + qsin(x) + rcos(x) + stan(x) + tx^2 + u) 
is monotonically decreasing or non-increasing over the domain ([0,1]).

And:
- f(x) is min when x = 1
- f(x) is max when x = 0

Since f(x) is monotonically decreasing over the domain ([0,1]) so we do binary search and
- if f(x) > 0, we increase x to make f(x) move close to 0
- if f(x) < 0, we decrease x to make f(x) move close to 0
"""
import math

p, q, r, s, t, u = 0, 0, 0, 0, -2, 1

def calcualte_f_x(x, p, q, r, s, t, u):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x**2 + u
# Use binary search to find the solution within the range [0, 1]

def find_x(p, q, r, s, t, u, left, right):    
    mid = 0
    for _ in range(100): # We can not do while left <= right because it will be infinitive, choose 100 as a loop is enough to get the result
        mid = (left + right) / 2
        if calcualte_f_x(mid, p, q, r, s, t, u) > 0:
            # increase x to make f(x) move close to 0
            left = mid
        else:
            # we decrease x to make f(x) move close to 0
            right = mid
    return mid

# Check if a solution within the specified range is found
left = 0
right = 1
x = find_x(p, q, r, s, t, u, left, right)
f_x = calcualte_f_x(x, p, q, r, s, t, u)
if abs(f_x) < 1e-9:
    print('{:0.4f}'.format(x))
else:
    print("No solution")











