# Python - Input/Output
---
> open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: `open(filename, mode, encoding=None)`
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be `r` when the file will only be read, `w` for only writing (an existing file with the same name will be erased), and `a` opens the file for appending; any data written to the file is automatically added to the end. `r+` opens the file for both reading and writing. The mode argument is optional; `r` will be assumed if it’s omitted.

``` python
f = open('workfile', 'w', encoding="utf-8")
```

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

``` python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
```
