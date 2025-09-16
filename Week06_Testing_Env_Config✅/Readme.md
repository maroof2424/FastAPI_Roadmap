# ✅ **Week 6: Testing + Environment Configs**

### **Goals**

* Learn unit & integration testing with `pytest` and FastAPI’s `TestClient`.
* Override dependencies for mocking DB/auth.
* Manage environment configs with `.env` and `python-dotenv`.
* Use `pydantic.BaseSettings` for clean configuration handling.

---

## 🔹 **Day 1 – Setup Testing**

**Goals:**

* Install `pytest`, `httpx`, `pytest-asyncio`.
* Create `tests/` folder.
* Write a simple test for `/health` route.

**Tasks:**

* Add `tests/test_basic.py`
* Use `TestClient` or `httpx.AsyncClient`.

---

## 🔹 **Day 2 – Dependency Overrides**

**Goals:**

* Mock DB session (`get_db`) for tests.
* Override `get_current_user` for protected routes.

**Tasks:**

* Use `app.dependency_overrides` in tests.
* Example: fake user instead of JWT in test mode.

---

## 🔹 **Day 3 – CRUD Route Testing**

**Goals:**

* Test `/users/` (signup) & `/posts/` (CRUD).
* Ensure DB transactions roll back after each test.

**Tasks:**

* Write `test_users.py`, `test_posts.py`.
* Use `setup_db` fixture to create/drop tables.

---

## 🔹 **Day 4 – Auth Route Testing**

**Goals:**

* Test `/auth/token` (login).
* Test `/users/me` (protected route).
* Use real JWT + fake user in tests.

**Tasks:**

* Use `TestClient` to call login route.
* Pass `Authorization: Bearer <token>` headers.

---

## 🔹 **Day 5 – Environment Configs**

**Goals:**

* Create `.env` file (`DB_URL`, `SECRET_KEY`, etc.).
* Load using `python-dotenv`.
* Define `settings.py` with `BaseSettings`.

**Tasks:**

* `config.py` with Pydantic `Settings` class.
* Import `settings` globally across project.

---

## 🔹 **Day 6 – Config Switching**

**Goals:**

* Separate configs: `Dev`, `Test`, `Prod`.
* Use `.env.test` for testing DB.

**Tasks:**

* `Settings` with environment variable `ENV`.
* Auto-load test DB when running pytest.

---

## 🔹 **Day 7 – Final Review**

**Goals:**

* Refactor configs & tests.
* Run all tests with `pytest -v --maxfail=1`.
* Generate coverage report.

**Tasks:**

* `pytest --cov=app tests/`
* Fix failing tests.
* Ensure config works for all environments.

---

### 📂 **Week 6 Directory**

```
Week06_Testing_Configs/
│── app/
│   ├── main.py
│   ├── config.py       # Pydantic BaseSettings
│── tests/
│   ├── conftest.py     # fixtures
│   ├── test_basic.py
│   ├── test_users.py
│   ├── test_posts.py
│   ├── test_auth.py
│── .env
│── .env.test
│── pytest.ini
```

---
