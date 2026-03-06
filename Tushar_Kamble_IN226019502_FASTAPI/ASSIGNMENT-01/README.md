
# FastAPI Assignment 1
## Overview

This project is part of the FastAPI Internship Training – Day 1 Assignment.
The goal of this assignment is to build basic API endpoints using FastAPI and perform operations like filtering, searching, and summarizing product data.

The APIs simulate a simple E-commerce Product Management System.

# Technologies Used

Python 3

FastAPI

Uvicorn

Swagger UI

# Setup Instructions
1. Create Virtual Environment
python -m venv venv
2. Activate Virtual Environment

Windows:

venv\Scripts\activate
3. Install Dependencies
pip install fastapi uvicorn
4. Run FastAPI Server
uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs
* API Endpoints
1. Get All Products
GET /products

Returns the complete list of products and total count.

2. Filter Products by Category
GET /products/category/{category_name}

Example:

/products/category/Electronics

Returns products belonging to the specified category.

3. Get In-Stock Products
GET /products/instock

Returns only the products that are currently available in stock.

4. Store Summary
GET /store/summary

Returns store information including:

Total products

In-stock products

Out-of-stock products

Available categories

5. Search Products
GET /products/search/{keyword}

Search products by name (case-insensitive).

Example:

/products/search/mouse

# Bonus Endpoint
Best Deal & Premium Pick
GET /products/deals

Returns:

Cheapest product (Best Deal)

Most expensive product (Premium Pick)


# Learning Outcomes

Through this assignment, the following concepts were practiced:

FastAPI application setup

API endpoint creation

Path parameters

Data filtering using Python

Case-insensitive search

Basic API design principles
