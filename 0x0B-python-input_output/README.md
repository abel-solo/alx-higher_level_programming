# Python - Input/Output
---
> open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: `open(filename, mode, encoding=None)`
``` python
f = open('workfile', 'w', encoding="utf-8")
```

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:
