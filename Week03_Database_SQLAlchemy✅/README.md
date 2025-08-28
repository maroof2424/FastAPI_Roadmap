# 🗓️ **Week 3 – SQLAlchemy & Database Integration **

---

### **🔹 Day 1 – Setup Database & Models**

**Goals:**

* Install SQLAlchemy
* Configure SQLite DB
* Create Base + Engine
* Define `User` & `Post` models

**Tasks:**

* `database.py` → engine & session config
* `models.py` → SQLAlchemy models (`User`, `Post`)

---

### **🔹 Day 2 – Pydantic Schemas for DB**

**Goals:**

* Separate Pydantic schemas from ORM models
* Create request (`PostCreate`, `UserCreate`) & response (`PostOut`, `UserOut`) schemas

**Tasks:**

* Update `schemas.py` for DB-backed models
* Handle ORM → Pydantic conversion (`orm_mode = True`)

---

### **🔹 Day 3 – Dependency Injection (DB Session)**

**Goals:**

* Learn `SessionLocal` & `get_db` dependency
* Inject session into routes

**Tasks:**

* Add `get_db` in `database.py`
* Update routers to use `db: Session = Depends(get_db)`

---

### **🔹 Day 4 – CRUD with Database**

**Goals:**

* Move CRUD from Python lists → real SQL queries
* Implement:

  * `create_user`
  * `get_user`
  * `create_post`
  * `get_posts`

**Tasks:**

* Use SQLAlchemy ORM queries (`db.query()`)
* Commit + refresh objects

---

### **🔹 Day 5 – Relationships (One-to-Many)**

**Goals:**

* Connect `User` ↔ `Post` (1 user = many posts)
* Use `relationship()` in SQLAlchemy

**Tasks:**

* Update `models.py` with relationships
* Add `author_id` foreign key in posts
* Test fetching posts by user

---

### **🔹 Day 6 – Migrations (Alembic Intro)**

**Goals:**

* Setup Alembic for migrations
* Generate migration for `User` & `Post`

**Tasks:**

* Initialize Alembic
* Run `alembic revision --autogenerate`
* Apply migration with `alembic upgrade head`

---

### **🔹 Day 7 – Mini Project: Blog API with Database**

**Goals:**

* Refactor Blog API to use SQLAlchemy
* Endpoints:

  * `POST /users`
  * `GET /users/{id}`
  * `POST /posts`
  * `GET /posts`
* Response models with nested relationships (`User → Posts`)

**Tasks:**

* Integrate all CRUD with DB
* Test thoroughly in Swagger

---
