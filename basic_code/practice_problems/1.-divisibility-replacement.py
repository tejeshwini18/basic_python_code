"""Print values from 1 to 50 with replacements.
- divisible by 3 -> foo
- divisible by 5 -> bar
- divisible by 15 -> hello
"""

results = []
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        results.append("hello")
    elif i % 3 == 0:
        results.append("foo")
    elif i % 5 == 0:
        results.append("bar")
    else:
        results.append(i)

print(results)
