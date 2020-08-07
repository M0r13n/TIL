# TIL about SQL

### Aggregates
An aggregate functions takes a **bag** (*unordered*, *non-unique* *tuples*) can produces a **single scalar value**. A **scalar function** produces a **single value** from any given input.

- `SELECT count(*) FROM student WHERE student.id > 1000;` <- `count(*)` is the aggregate

If an aggregate is used other functions that are **not** aggregates need to be **aggregated**.

Does not work because `e.cid` is not aggregated: 

```sql
SELECT AVG(s.gpa), e.cid 
FROM enrolled AS e, student AS s
WHERE e.sid = s.sid;
```

Does work:

```sql
SELECT AVG(s.gpa), e.cid 
    FROM enrolled AS e, student AS s
    WHERE e.sid = s.sid
GROUP BY e.cid;
```

It is also possible to filter **after** an aggregation:

```sql
SELECT AVG(s.gpa)  AS avg_gpa , e.cid 
    FROM enrolled AS e, student AS s
    WHERE e.sid = s.sid
    GROUP BY e.cid
HAVING avg_gpa >= 1000;
```


# Nested queries
When nesting queries the **inner** query can access attributes from the **outer** query. But the outer cannot access anything from the inner.