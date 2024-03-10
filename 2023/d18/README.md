# Day18

The problem asks to calculate the area (perimeter included) of a grided-shape.

# How to proceed

To calculate the area, see [this](https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdveugr/?utm_source=share&utm_medium=web2x&context=3) comment:

**[Gauss's area formula](https://en.wikipedia.org/wiki/Shoelace_formula) (special case of Green's theorem) + [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)**

The Pick's theorem formula needs some manipulation. 
Pick's theorem says that A = i + b / 2 - 1, where **A** is the area of the polygon, **i** is the number of internal integer points, and **b** is the number of boundary integer points.

We can calculate the **Area** from the *Gauss's area formula* (Shoelace Formula), whereas boundary points (**b**) could be calculated by measuring the perimeter distance.

Thus our formula is:

```
(A - b/2 + 1) = i
```

Add the perimeter, since those boundary points are also counted.
