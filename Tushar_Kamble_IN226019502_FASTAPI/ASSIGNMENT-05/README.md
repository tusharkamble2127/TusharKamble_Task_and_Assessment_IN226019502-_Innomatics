# FastAPI Search, Sort & Pagination – Day 6 Assignment

##  Project Overview

This project extends the FastAPI E-commerce system with **Search, Sorting, and Pagination features**.

It simulates real-world API behavior where users can:

* Search products
* Sort results
* Navigate pages
* Combine all features in a single endpoint

Assignment reference: 

---

#  Features Implemented

##  Search

* Case-insensitive product search
* Friendly message for no results

##  Sorting

* Sort by:

  * Price (asc/desc)
  * Name (A–Z / Z–A)
* Invalid sort field handled with error

##  Pagination

* Page-wise product browsing
* Custom page & limit support
* Total pages calculation

##  Combined API (Browse)

* Search + Sort + Pagination in one API

##  Orders Search

* Search orders by customer name (case-insensitive)

##  Bonus

* Orders pagination

---

#  Installation

```bash
pip install fastapi uvicorn
```

Run server:

```bash
uvicorn main:app --reload
```

---

#  API Docs

```text
http://127.0.0.1:8000/docs
```

---

#  Test Results (Checklist)

## Q1 — Search

✔ "mouse" and "MOUSE" return same result
✔ Case-insensitive working
✔ "laptop" shows no-results message

---

## Q2 — Sorting

✔ Price ascending → Pen Set first
✔ Price descending → USB Hub first
✔ Name sorting works
✔ Invalid sort_by returns error

---

## Q3 — Pagination

✔ Page 1 & 2 different
✔ Page 3 empty list
✔ limit=1 → total_pages = 4

---

## Q4 — Orders Search

✔ Case-insensitive search works
✔ Correct orders returned

---

## Q5 — Sort by Category + Price

✔ Electronics shown first
✔ Within category → sorted by price

---

## Q6 — Combined Browse API

✔ Works with all parameters
✔ Default → all products sorted by price asc

---

##  Bonus — Orders Pagination

✔ Orders correctly paginated
✔ total_pages calculated correctly

---

#  API Endpoints

##  Search Products

```
GET /products/search?keyword=mouse
```

---

##  Sort Products

```
GET /products/sort?sort_by=price&order=asc
```

---

##  Pagination

```
GET /products/page?page=1&limit=2
```

---

##  Orders Search

```
GET /orders/search?customer_name=rahul
```

---

##  Sort by Category

```
GET /products/sort-by-category
```

---

##  Browse (Search + Sort + Pagination)

```
GET /products/browse?keyword=e&sort_by=price&order=asc&page=1&limit=2
```

---

##  Orders Pagination

```
GET /orders/page?page=1&limit=3
```

---

#  Example Output

```json
{
 "keyword": "mouse",
 "total_found": 1,
 "products": [
   {
     "name": "Wireless Mouse",
     "price": 499
   }
 ]
}
```


