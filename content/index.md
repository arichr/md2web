Title: Welcome ✨
---
# md2web
Flask server to render Markdown files.
# Why?
I need a small server to serve my Markdown files, but using frameworks is too complicated for this task.
# Features
 * Light
 * Easy to use
 * Caches results
 * Built on top of [python-markdown](https://python-markdown.github.io)
# Enabled extensions
External:

* [Automatic header demoting](https://github.com/SaschaCowley/Markdown-Headdown)

Internal:

* [Admonitions](https://python-markdown.github.io/extensions/admonition/)
* [CodeHilite (Code highlighting)](https://python-markdown.github.io/extensions/code_hilite/)
* [Definition list](https://python-markdown.github.io/extensions/definition_lists/)
* [Fenced code blocks](https://python-markdown.github.io/extensions/fenced_code_blocks/)
* [Meta-Data](https://python-markdown.github.io/extensions/meta_data/)
* [New Line to Break](https://python-markdown.github.io/extensions/nl2br/)
* [Tables](https://python-markdown.github.io/extensions/tables/)
* [TOC (Table of Contents)](https://python-markdown.github.io/extensions/toc/)
* [Sane lists](https://python-markdown.github.io/extensions/sane_lists/)

# Testing area
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

!!! danger "Danger!"
    This is an example!
!!! note
    Notes are great.
!!! warning "A danger nearby..."
    Look closely.

| Tables | are | great |
|--------|:---:|------:|
| **1**  | _2_ |  `3`  |

Apple
:   Pomaceous fruit of plants of the genus Malus in
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

This will be
on the next line.

* One
* Two

1. Three?
2. Four?

* Five?

[TOC]
