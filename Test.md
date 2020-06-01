## doctest

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
```

run_docstring_examples(function_name, globals(), verbose output)
When the return value of a function does not match the expected result, the run_docstring_examples function will report this problem as a test failure.

