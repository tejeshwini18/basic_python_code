"""Build an even/odd label list from 0..10."""

even_numbers = ["even" if i % 2 == 0 else "odd" for i in range(11)]
print(even_numbers)
