SELECT owner_id, owner_name, COUNT(category_id) AS different_category_count
FROM owner NATURAL JOIN (SELECT DISTINCT category_id, article_id
                            FROM article NATURAL JOIN category_article_mapping)
GROUP BY owner_id, owner_name
ORDER BY COUNT(category_id) DESC;

