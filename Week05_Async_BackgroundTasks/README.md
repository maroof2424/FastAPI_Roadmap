# 🗓️ Week 5 – Async Programming + Background Tasks (FastAPI)

## 🎯 Goals
- Understand **async I/O** in FastAPI
- Learn how to run **background jobs**
- Explore async **database queries** and **HTTP requests**

---

## 📘 Topics Covered

### ✅ Day 1 – Async Endpoints
- Using `async def` in FastAPI
- Awaiting async tasks
- Difference between sync vs async endpoints
- 📂 File: `app/endpoints.py`

---

### ✅ Day 2 – Async Database
- Setup async database (Postgres with `asyncpg` or `databases`)
- Async CRUD operations
- 📂 File: `app/db.py`

---

### ✅ Day 3 – Background Tasks
- Using FastAPI’s `BackgroundTasks`
- Example: simulate sending an email in the background
- 📂 File: `app/tasks.py`

---

### ✅ Day 4 – Async HTTP Requests
- Install & use `httpx`
- Fetch data from an external API asynchronously
- 📂 File: `app/utils.py`

---

### ✅ Day 5–6 – Mini Project
- Build an API that:
  - Fetches external data (async with `httpx`)
  - Stores it in DB (async insert)
  - Simulates background job (email notification)
- 📂 Files: `app/main.py`, `05_mini_project`

---

### ✅ Day 7 – Review & Testing
- Unit tests with pytest + httpx test client
- 📂 Files: `tests/test_endpoints.py`, `tests/test_tasks.py`

---

## 📦 Project Outcome
By the end of Week 5, you will have:
- Async REST API with FastAPI
- Async DB integration
- Background task system
- External API integration
- Unit tested endpoints

