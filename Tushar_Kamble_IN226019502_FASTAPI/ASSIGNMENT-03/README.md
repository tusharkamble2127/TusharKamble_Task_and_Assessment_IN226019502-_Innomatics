# FastAPI Assignment – Day 1, Day 2 & Day 4

##  Project Overview

This project is a **FastAPI-based E-commerce API** built during the internship training program.
The API provides product management, filtering, analytics, and CRUD operations for an online store.

The project combines features from:

* Day 1 – Basic API endpoints
* Day 2 – Filtering, feedback system, and bulk orders
* Day 4 – Full CRUD operations and inventory audit

The API is tested using **Swagger UI**.

---

# Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn
* Swagger UI

---

# Installation

Clone the repository:

```
git clone https://github.com/your-username/your-repository-name.git
```

Navigate to the project folder:

```
cd your-repository-name
```

Install dependencies:

```
pip install fastapi uvicorn
```

Run the server:

```
uvicorn main:app --reload
```

---

# API Documentation

Open Swagger UI in your browser:

```
http://127.0.0.1:8000/docs
```

---

# Initial Product Data

```
1  Wireless Mouse  | 499 | Electronics | In Stock
2  Notebook        |  99 | Stationery  | In Stock
3  USB Hub         | 799 | Electronics | Out of Stock
4  Pen Set         |  49 | Stationery  | In Stock
```

---

# Day 1 APIs

| Method | Endpoint                             | Description                            |
| ------ | ------------------------------------ | -------------------------------------- |
| GET    | `/products`                          | Get all products                       |
| GET    | `/products/category/{category_name}` | Filter products by category            |
| GET    | `/products/instock`                  | Show only available products           |
| GET    | `/store/summary`                     | Store statistics                       |
| GET    | `/products/search/{keyword}`         | Search product by name                 |
| GET    | `/products/deals`                    | Show cheapest & most expensive product |

---

# Day 2 APIs

| Method | Endpoint                       | Description                 |
| ------ | ------------------------------ | --------------------------- |
| GET    | `/products/filter`             | Filter by price or category |
| GET    | `/products/{product_id}/price` | Get product price only      |
| POST   | `/feedback`                    | Submit customer feedback    |
| GET    | `/products/summary`            | Product analytics dashboard |
| POST   | `/orders/bulk`                 | Bulk order system           |
| POST   | `/orders`                      | Place order                 |
| GET    | `/orders/{order_id}`           | Get order details           |
| PATCH  | `/orders/{order_id}/confirm`   | Confirm order               |

---

# Day 4 APIs (CRUD)

| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| POST   | `/products`              | Add a new product      |
| PUT    | `/products/{product_id}` | Update product         |
| DELETE | `/products/{product_id}` | Delete product         |
| GET    | `/products/audit`        | Inventory audit report |

---

# Bonus Feature

| Method | Endpoint             | Description                  |
| ------ | -------------------- | ---------------------------- |
| PUT    | `/products/discount` | Apply category-wide discount |

Example request:

```
PUT /products/discount?category=Electronics&discount_percent=10
```

This reduces the price of all products in the selected category.

---

# Example Audit Response

```
{
  "total_products": 4,
  "in_stock_count": 3,
  "out_of_stock_names": ["USB Hub"],
  "total_stock_value": 6470,
  "most_expensive": {
    "name": "USB Hub",
    "price": 799
  }
}
```

---

# Features Implemented

* Product listing
* Category filtering
* Inventory tracking
* CRUD operations
* Customer feedback system
* Bulk order processing
* Product analytics
* Inventory audit API
* Category discount system

-----------------------------------------------


