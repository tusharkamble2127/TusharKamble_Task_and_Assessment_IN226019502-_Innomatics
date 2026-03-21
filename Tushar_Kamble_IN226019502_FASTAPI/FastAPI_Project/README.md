#  Gym Management System (FastAPI Project)

##  Project Overview
This project is a complete backend system built using FastAPI.  
It manages gym membership plans, enrollments, and class bookings.

---

##  Features Implemented

###  Day 1 – GET APIs
- Home route
- Get all plans
- Get plan by ID
- Membership list
- Plans summary

###  Day 2 – POST + Pydantic
- Membership enrollment
- Input validation using Pydantic

###  Day 3 – Helper Functions
- find_plan()
- calculate_membership_fee()
- filter_plans_logic()

###  Day 4 – CRUD Operations
- Add new plan
- Update plan
- Delete plan (with validation)

###  Day 5 – Multi-Step Workflow
- Class booking system
- Cancel booking
- Freeze & Reactivate membership

###  Day 6 – Advanced APIs
- Search plans
- Sort plans
- Pagination
- Combined browse endpoint

---

##  Technologies Used
- Python
- FastAPI
- Uvicorn
- Pydantic

---

##  How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
