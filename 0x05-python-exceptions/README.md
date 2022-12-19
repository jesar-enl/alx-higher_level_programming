# EXCEPTION HANDLING IN PYTHON

Exceptions are handled using the `try...except` format whereby the `try` part holds the code to be executed while the `except` part deals with the exception that is to be handled.

## Example

```python
try:
	a, b = 12, 0
	print(a / b)
except Exception as err:
	print("Cannot divide by 0")
```

This will result into:
`Cannot divide by 0`
