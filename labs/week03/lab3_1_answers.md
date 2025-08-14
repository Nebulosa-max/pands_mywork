# Lab 3.1 – Extra Questions and Answers

## Q6 – Why does this expression cause an error? How can you fix it?

**Code:**
```python
message = 'I have eaten ' + 99 + ' burritos.'
print(message)

Reason for error:
In Python, you cannot concatenate (join) a string and an integer directly.
'I have eaten ' is a string, but 99 is an integer.

Fix: Convert the integer to a string or use an f-string.

Example fixes:

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# or using f-string:
message = f'I have eaten {99} burritos.'
print(message)

Q7 – Why is eggs a valid variable name while 100 is invalid?
	•	Variable names must start with a letter or underscore (_), not a digit.
	•	eggs ✅ valid – starts with a letter.
	•	100 ❌ invalid – starts with a number.

⸻

Q8 – What three functions can be used to get the integer, floating-point number, or string version of a value?
	•	int() → converts to an integer.
	•	float() → converts to a floating-point number.
	•	str() → converts to a string.