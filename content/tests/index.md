Title: Tests
---

[TOC]

# Code blocks

```
from typing import Iterator

# This is an example
class Math:
    @staticmethod
    def fib(n: int) -> Iterator[int]:
        """ Fibonacci series up to n """
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b

result = sum(Math.fib(42))
print("The answer is {}".format(result))
```

# Admonitions

!!! danger "Danger!"
    This is an example!
!!! note
    Notes are great.
!!! warning "A danger nearby..."
    Look closely.

# Tables

| Tables | are | great |
|--------|:---:|------:|
| **1**  | _2_ |  `3`  |

# Definitions

Apple
:   Pomaceous fruit of plants of the genus Malus in
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

1. One

This will be
on the next line.

2. Two
3. Three
