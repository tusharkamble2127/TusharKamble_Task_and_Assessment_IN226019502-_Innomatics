from fastapi import FastAPI, Query, HTTPException
from typing import Optional

app = FastAPI()

# ---------------- PRODUCTS ----------------
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
]

# ---------------- ORDERS ----------------
orders = []
order_id_counter = 1


# Q1 — SEARCH PRODUCTS
@app.get("/products/search")
def search_products(keyword: str = Query(...)):
    result = [p for p in products if keyword.lower() in p["name"].lower()]

    if not result:
        return {"message": f"No products found for: {keyword}"}

    return {
        "keyword": keyword,
        "total_found": len(result),
        "products": result
    }

# Q2 — SORT PRODUCTS
@app.get("/products/sort")
def sort_products(
    sort_by: str = Query("price"),
    order: str = Query("asc")
):
    if sort_by not in ["price", "name"]:
        return {"error": "sort_by must be 'price' or 'name'"}

    reverse = (order == "desc")

    sorted_products = sorted(products, key=lambda p: p[sort_by], reverse=reverse)

    return {
        "sort_by": sort_by,
        "order": order,
        "products": sorted_products
    }

# Q3 — PAGINATION
@app.get("/products/page")
def paginate_products(
    page: int = Query(1, ge=1),
    limit: int = Query(2, ge=1)
):
    start = (page - 1) * limit
    end = start + limit

    total = len(products)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": -(-total // limit),
        "products": products[start:end]
    }

# Q4 — ORDERS + SEARCH
@app.post("/orders")
def create_order(customer_name: str = Query(...)):
    global order_id_counter

    order = {
        "order_id": order_id_counter,
        "customer_name": customer_name
    }

    orders.append(order)
    order_id_counter += 1

    return {"message": "Order created", "order": order}


@app.get("/orders/search")
def search_orders(customer_name: str = Query(...)):
    result = [
        o for o in orders
        if customer_name.lower() in o["customer_name"].lower()
    ]

    if not result:
        return {"message": f"No orders found for: {customer_name}"}

    return {
        "customer_name": customer_name,
        "total_found": len(result),
        "orders": result
    }

# Q5 — SORT BY CATEGORY + PRICE
@app.get("/products/sort-by-category")
def sort_by_category():
    result = sorted(products, key=lambda p: (p["category"], p["price"]))

    return {
        "products": result,
        "total": len(result)
    }

# Q6 — BROWSE (SEARCH + SORT + PAGINATION)
@app.get("/products/browse")
def browse_products(
    keyword: Optional[str] = None,
    sort_by: str = Query("price"),
    order: str = Query("asc"),
    page: int = Query(1, ge=1),
    limit: int = Query(4, ge=1)
):
    result = products

    # SEARCH
    if keyword:
        result = [p for p in result if keyword.lower() in p["name"].lower()]

    # SORT
    if sort_by in ["price", "name"]:
        result = sorted(result, key=lambda p: p[sort_by], reverse=(order == "desc"))

    # PAGINATION
    total = len(result)
    start = (page - 1) * limit
    end = start + limit

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_found": total,
        "total_pages": -(-total // limit),
        "products": result[start:end]
    }

# BONUS — ORDERS PAGINATION
@app.get("/orders/page")
def paginate_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(3, ge=1)
):
    start = (page - 1) * limit
    end = start + limit

    total = len(orders)

    return {
        "page": page,
        "limit": limit,
        "total_orders": total,
        "total_pages": -(-total // limit),
        "orders": orders[start:end]
    }