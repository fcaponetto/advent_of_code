# How to get a transpose of a matrix

```python
p = [*zip(*p)]
```

# Why does it work?
The **zip** function takes iterables as arguments and aggregates them. By passing *p, we are effectively passing each row of p as a separate iterable to zip.
```python
p = [[1, 2, 3], 
     [4, 5, 6]]

*p = [1, 2, 3], [4, 5, 6]

zip(*p) = 
zip([1, 2, 3], 
    [4, 5, 6]) =

    (1, 4), 
    (2, 5), 
    (3, 6)

[*zip(*p)] = [(1, 4), 
              (2, 5), 
              (3, 6)] # traspose
```

If you need a list, then:
```python
p = [[1, 2, 3], 
     [4, 5, 6]]

[list(row) for row in zip(*p)] =
    [[1, 4], 
     [2, 5], 
     [3, 6]]

```