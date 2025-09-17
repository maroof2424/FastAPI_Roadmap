

# 📅 Week 7: Docker + Deployment Roadmap

### ✅ Goals

* Dockerize your FastAPI project.
* Use `docker-compose` for API + DB.
* Run with production settings (Gunicorn/Uvicorn workers).
* Deploy to free cloud service (Render, Fly.io, or DigitalOcean).

---

## 📂 Day 1 – Dockerfile

Create a `Dockerfile` in the project root:

```dockerfile
# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run Uvicorn (dev mode)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📂 Day 2 – Docker Compose

`docker-compose.yml` for API + Postgres DB:

```yaml
version: "3.9"

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: fastapi_user
      POSTGRES_PASSWORD: fastapi_pass
      POSTGRES_DB: fastapi_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  api:
    build: .
    restart: always
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql+asyncpg://fastapi_user:fastapi_pass@db:5432/fastapi_db
      ENV: prod
    ports:
      - "8000:8000"

volumes:
  postgres_data:
```

Run:

```bash
docker-compose up --build
```

---

## 📂 Day 3 – Production Server (Gunicorn + Uvicorn workers)

Install:

```bash
pip install "uvicorn[standard]" gunicorn
```

Update `Dockerfile` CMD:

```dockerfile
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:8000", "-w", "4"]
```

* `-w 4` → 4 workers (adjust per CPU).
* This makes the API **production-ready**.

---

## 📂 Day 4–5 – Deployment

### Render (simplest free tier)

1. Push code to GitHub.
2. Create new **Web Service** on Render.
3. Choose repo + Python environment.
4. Add build command:

   ```bash
   pip install -r requirements.txt
   ```
5. Start command:

   ```bash
   gunicorn -k uvicorn.workers.UvicornWorker app.main:app -w 4 -b 0.0.0.0:8000
   ```
6. Add Postgres DB in Render dashboard → set `DATABASE_URL`.

---

### Fly.io (alternative free tier)

1. Install Flyctl:

   ```bash
   curl -L https://fly.io/install.sh | sh
   flyctl auth login
   ```
2. Initialize app:

   ```bash
   flyctl launch
   ```
3. Deploy:

   ```bash
   flyctl deploy
   ```

---

## 📂 Day 6 – Environment Variables

* Store secrets (`SECRET_KEY`, `DATABASE_URL`) in Render/Fly dashboard.
* Remove `.env` from production build.

---

## 📂 Day 7 – Final Review

* Run container locally: `docker-compose up`.
* Run tests inside container:

  ```bash
  docker-compose run --rm api pytest
  ```
* Verify deployment on Render/Fly.io (public URL).

---

✅ End of Week 7 Deliverable:

* A fully **containerized FastAPI CRUD API**.
* Deployed live to Render/Fly.io with Postgres DB.

---
