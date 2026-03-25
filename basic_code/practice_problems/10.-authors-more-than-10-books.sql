-- Find authors who have written more than 10 books.
SELECT author
FROM BookAuthor
GROUP BY author
HAVING COUNT(book) > 10;
