## Doctest

In Python, simple test cases can be put in functions, but must be in the beginning. A description of function and followed by a new line, then test cases. The format is shown below. Test case and expected result shall be put on separate lines.

```
def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total

if __name__ == "__main__":
    import doctest
    doctest.testmod() // If test examples are in the example.txt file, use this: doctest.testfile("example.txt")
```



Run it with commands: "python3 -m doctest <python_source_file> -v". Without '-v', it doesn't have output unless there's failure.

run_docstring_examples(function_name, globals(), verbose output true or not) tests single function.
When the return value of a function does not match the expected result, the run_docstring_examples function will report this problem as a test failure.

This tests each function, so it's also called unit test.
