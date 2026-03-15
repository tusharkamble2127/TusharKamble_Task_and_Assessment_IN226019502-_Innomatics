# FastAPI Cart System – Day 5 Assignment

##  Project Overview

This project implements a **Shopping Cart System using FastAPI**.
Users can add products to the cart, view cart contents, remove items, and checkout to create orders.

The API simulates a simple **E-commerce cart workflow** using in-memory storage.

---

#  Features

* Add products to cart
* View cart items and grand total
* Prevent adding out-of-stock products
* Update quantity if the same product is added again
* Remove items from cart
* Checkout to create orders
* View all placed orders
* Handle empty cart checkout errors

---

#  Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* Swagger UI (API testing)

---

#  API Documentation

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

All endpoints can be tested directly from Swagger.

---

#  Initial Product Data

| ID | Product        | Price | Category    | Stock        |
| -- | -------------- | ----- | ----------- | ------------ |
| 1  | Wireless Mouse | ₹499  | Electronics | In Stock     |
| 2  | Notebook       | ₹99   | Stationery  | In Stock     |
| 3  | USB Hub        | ₹799  | Electronics | Out of Stock |
| 4  | Pen Set        | ₹49   | Stationery  | In Stock     |

---

#  API Endpoints

## Add Product to Cart

```
POST /cart/add
```

Example:

```
/cart/add?product_id=1&quantity=2
```

Response:

```json
{
 "message": "Added to cart",
 "cart_item": {
   "product_id": 1,
   "product_name": "Wireless Mouse",
   "quantity": 2,
   "unit_price": 499,
   "subtotal": 998
 }
}
```

---

## View Cart

```
GET /cart
```

Example response:

```json
{
 "items": [...],
 "item_count": 2,
 "grand_total": 1097
}
```

---

## Remove Item from Cart

```
DELETE /cart/{product_id}
```

Example:

```
DELETE /cart/2
```

Response:

```json
{
 "message": "Product 2 removed from cart"
}
```

---

## Checkout Cart

```
POST /cart/checkout
```

Request body:

```json
{
 "customer_name": "Ravi Kumar",
 "delivery_address": "MG Road Bangalore"
}
```

Response:

```json
{
 "orders_placed": [...],
 "grand_total": 1497
}
```

---

## View Orders

```
GET /orders
```

Example response:

```json
{
 "orders": [...],
 "total_orders": 3
}
```

---

#  Error Handling

| Scenario                 | Response        |
| ------------------------ | --------------- |
| Product not found        | 404 Not Found   |
| Out-of-stock product     | 400 Bad Request |
| Checkout with empty cart | 400 Bad Request |

Example error:

```json
{
 "detail": "USB Hub is out of stock"
}
```

---

#  Bonus Feature

The API prevents checkout when the cart is empty.

Example response:

```json
{
 "detail": "Cart is empty — add items first"
}
```

---

#  Example Cart Flow

1. Add Wireless Mouse (qty 2)
2. Add Notebook (qty 1)
3. View cart → grand_total = 1097
4. Update quantity of mouse
5. Remove Notebook
6. Checkout
7. View orders

---


