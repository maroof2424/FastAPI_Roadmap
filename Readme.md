# 🗓️ FastAPI Learning Plan – Week-by-Week (7 Weeks)

---

### ✅ **Week 1: FastAPI Fundamentals**

**Goals:**

* Understand FastAPI’s core structure
* Learn request/response cycle
* Learn Pydantic basics

**Topics:**

* Installing FastAPI + Uvicorn
* GET, POST routes
* Path & query parameters
* Request bodies with Pydantic
* Response models
* Built-in Swagger docs

**Build:**

* Simple product/item catalog API

**Resources:**

* [https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)
* YouTube: *FastAPI Crash Course – Traversy Media*

---

### ✅ **Week 2: CRUD + Pydantic + Routers**

**Goals:**

* Master full CRUD APIs
* Structure your code (routers, services)
* Learn response modeling

**Topics:**

* PUT, DELETE methods
* `APIRouter` for modular routing
* Path vs body data handling
* Pydantic field validation
* Optional parameters

**Build:**

* Blog API with `/posts`, `/posts/{id}`, etc.
* Use response models to hide internal fields

**Resources:**

* [https://fastapi.tiangolo.com/tutorial/body/](https://fastapi.tiangolo.com/tutorial/body/)

---

### ✅ **Week 3: Databases with SQLAlchemy**

**Goals:**

* Persist data with SQLAlchemy + SQLite
* Build models and CRUD operations

**Topics:**

* SQLAlchemy ORM
* Dependency injection for DB sessions
* Pydantic + SQLAlchemy conversion
* Create & migrate DB

**Build:**

* User + Post models with one-to-many relationship

**Resources:**

* [https://fastapi.tiangolo.com/tutorial/sql-databases/](https://fastapi.tiangolo.com/tutorial/sql-databases/)

---

### ✅ **Week 4: Authentication with JWT**

**Goals:**

* Build login/signup system
* Use OAuth2 with JWT

**Topics:**

* Password hashing (`passlib`)
* OAuth2PasswordBearer
* Token route (`/token`)
* Dependency-injected `get_current_user`

**Build:**

* Auth system with protected routes

**Resources:**

* [https://fastapi.tiangolo.com/tutorial/security/](https://fastapi.tiangolo.com/tutorial/security/)

---

### ✅ **Week 5: Async Programming + Background Tasks**

**Goals:**

* Understand async I/O in FastAPI
* Run background jobs

**Topics:**

* `async def` endpoints
* `asyncpg` or `Databases` library
* `BackgroundTasks` for jobs (e.g. email sending)
* Async HTTP calls with `httpx`

**Build:**

* API that fetches external data and stores it asynchronously
* Email simulation API (task queue pattern)

---

### ✅ **Week 6: Testing + Environment Configs**

**Goals:**

* Write unit/integration tests
* Manage environment configs

**Topics:**

* `pytest`, `TestClient`
* Dependency overrides for mocking
* `.env` with `python-dotenv`
* Config classes via Pydantic `BaseSettings`

**Build:**

* Write tests for auth, CRUD routes
* Use `.env` for DB credentials

---

### ✅ **Week 7: Docker + Deployment**

**Goals:**

* Dockerize your FastAPI project
* Deploy to cloud (Render, Fly.io, DigitalOcean)

**Topics:**

* Dockerfile + `uvicorn[standard]`
* `docker-compose` for DB + API
* Production server setup (Gunicorn workers)
* Render/Fly.io deployment (free tier)

**Build:**

* Containerized CRUD API

**Resources:**

* [https://fastapi.tiangolo.com/deployment/docker/](https://fastapi.tiangolo.com/deployment/docker/)

---



* GitHub CI to run `pytest` + lint on every push
* Instrumentation for metrics

---
