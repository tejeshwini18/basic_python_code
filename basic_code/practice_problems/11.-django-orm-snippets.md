# Django ORM snippets

```python
# Model - BookAuthor
BookAuthor.objects.all()
BookAuthor.objects.filter(author='')
BookAuthor.objects.get(book='')
BookAuthor.objects.get(book='').delete()
up_data = BookAuthor.objects.get(book='')
up_data.author = ''
```
