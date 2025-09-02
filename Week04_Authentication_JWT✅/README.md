# ✅ **Week 4: Authentication with JWT**

### 🎯 **Goals**

* Implement **signup + login** with JWT
* Use **hashed passwords** (never store plain text)
* Protect routes using `OAuth2PasswordBearer`
* Decode JWT and inject **current user**

---

## 📂 **Directory Structure**

```bash
Week04_Auth_JWT/
├── app/
│   ├── __init__.py
│   ├── database.py        # DB session
│   ├── models.py          # SQLAlchemy models (User, Post)
│   ├── schemas.py         # Pydantic schemas
│   ├── utils.py           # Password hashing (bcrypt)
│   ├── auth.py            # JWT creation & validation
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py       # User-related routes
│   │   ├── posts.py       # Post-related routes
│   │   ├── auth.py        # Auth routes (signup, login, me)
├── main.py                # FastAPI app entry
└── README.md
```

---

## 📅 **Day-by-Day Roadmap**

### 🔹 **Day 1 – Password Hashing**

* Install bcrypt:

  ```bash
  pip install passlib[bcrypt]
  ```
* `utils.py` → hash & verify password.

---

### 🔹 **Day 2 – Signup Route**

* `/auth/signup` → create user with hashed password.
* Schema: `UserCreate` with `password`.
* Return `UserOut` without password.

---

### 🔹 **Day 3 – JWT Token Setup**

* Install jose:

  ```bash
  pip install python-jose[cryptography]
  ```
* `auth.py` → create `create_access_token`.

---

### 🔹 **Day 4 – Login Route**

* `/auth/token` → check credentials, return JWT.
* Use `OAuth2PasswordRequestForm` for username/password.

---

### 🔹 **Day 5 – get\_current\_user Dependency**

* Decode JWT.
* Fetch user from DB.
* Raise `401 Unauthorized` if invalid.

---

### 🔹 **Day 6 – Protected Routes**

* Example: `/users/me` → return current user.
* Example: `/posts/` → only authenticated users can create.

---

### 🔹 **Day 7 – Cleanup & Test**

* Organize code into:

  * `utils.py` → password
  * `auth.py` → JWT
  * `routers/auth.py` → routes
* Test with Swagger (`/docs`) → use **Authorize** button.

---

⚡ End of Week 4 = You’ll have a real **signup/login system** with JWT + protected routes.

---