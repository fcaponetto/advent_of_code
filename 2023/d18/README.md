To calculate the area, see [this](https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdveugr/?utm_source=share&utm_medium=web2x&context=3) comment:

**Gauss's area formula (special case of Green's theorem) + Pick's theorem**

The formula given on the [Wiki page](https://en.wikipedia.org/wiki/Pick%27s_theorem) needs some manipulation. 
Pick's theorem says that A = i + b / 2 - 1, where **A** is the area of the polygon, **i** is the number of internal integer points, and **b** is the number of boundary integer points.

We have **Area** from the *Gauss's area formula* (Shoelace Formula), and we have the number of boundary points (**b**) with the perimeter. We want the internal points, so we have some algebra to do.

Solve for i by subtracting b/2 - 1 from both sides, getting i = A - b / 2 + 1. Note from the given example that you can get the number of enclosed points (Day 10!) with just this formula. But we have a little more work to do.

Add the perimeter, since those boundary points are also counted.

Thus our formula is
```
A - b / 2 + 1 + b = A + b / 2 + 1
```

```
(A - b/2 + 1) = i
```