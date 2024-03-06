-- 코드를 입력하세요
SELECT b.book_id, a.author_name, TO_CHAR(b.published_date, 'YYYY-MM-DD') AS published_date
FROM book b , author a
WHERE b.author_id = a.author_id
AND b.category = '경제'
ORDER BY published_date;