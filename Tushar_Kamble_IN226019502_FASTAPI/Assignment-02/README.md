# FastAPI Assignment 2 – Advanced API Features
## Overview

This project is part of the FastAPI Internship Training – Day 2 Assignment.
The goal of this assignment is to extend the existing Day-1 e-commerce API by implementing additional endpoints and features such as query filtering, product summaries, feedback submission, and bulk order processing.

The APIs simulate a simple E-commerce backend system with product management and order handling.

## Technologies Used

    Python 3
    
    FastAPI
    
    Uvicorn
    
    Pydantic
    
    Swagger UI

## Setup Instructions
1️. Create Virtual Environment

python -m venv venv

2️. Activate Environment

Windows:

venv\Scripts\activate

3️. Install Dependencies
pip install fastapi uvicorn

4️. Run FastAPI Server
uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs

🔹 Implemented API Endpoints

1️. Filter Products by Price
GET /products/filter

Allows filtering products using query parameters.

Example:

/products/filter?min_price=400

2️. Get Product Price
GET /products/{product_id}/price

Returns only the name and price of the selected product.

3️. Submit Customer Feedback
POST /feedback

Accepts customer feedback using a Pydantic model with validation.

Fields:

customer_name

product_id

rating (1–5)

comment (optional)

4️. Product Summary Dashboard
GET /products/summary

Returns store analytics including:

Total products

In-stock products

Out-of-stock products

Cheapest product

Most expensive product

Available categories

5️. Bulk Order Processing
POST /orders/bulk

Allows companies to place bulk orders.

Features:

Multiple items per order

Stock validation

Failed items reporting

Grand total calculation

** Bonus Feature – Order Status Tracking

Additional endpoints for managing order status.

Create Order
POST /orders

New orders start with:

status = "pending"
Get Order Details
GET /orders/{order_id}

Returns order information.

Confirm Order
PATCH /orders/{order_id}/confirm

Changes order status from:

pending → confirmed
## Output Screenshots

Screenshots are included for each API endpoint execution:

Q1A_Output.png
Q1B_Output.png
Q1C_Output.png

Q2A_Output.png
Q2B_Output.png

Q3_Output.png

Q4_Output.png

Q5A_Output.png
Q5B_Output.png

Bonus_Pending_Output.png
Bonus_Confirm_Output.png

Bonus_Output.png

## Learning Outcomes

Through this assignment, the following FastAPI concepts were practiced:

1.Query Parameters

2.Path Parameters

3.POST Requests

4.PATCH Requests

5.Pydantic Validation

6.Business Logic Implementation

API Testing using Swagger UI
